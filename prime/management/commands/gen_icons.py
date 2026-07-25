"""Regenerate the whole Powerty icon set (favicons + PWA icons) from the master logo.

Source: `static/images/finlogo.png` — the panda head ringed by two growth arrows on
a cream field. The command crops to the *linework*, not to the cream circle around
it, so the panda fills the icon instead of floating in padding: at Google-result and
browser-tab sizes that difference is the whole ballgame.

    python manage.py gen_icons
    python manage.py gen_icons --source images/other_logo.png

Dev-only helper — the generated PNG/ICO files are committed to the repo, so
production never needs to run this.
"""

from collections import deque
from pathlib import Path

from django.conf import settings
from django.core.management.base import BaseCommand, CommandError

DEFAULT_SOURCE = 'images/finlogo.png'

# How much of the icon the artwork spans, measured as the radius of the smallest
# circle containing it. 0.46 keeps a hair of breathing room inside a circular
# crop — Google Search rounds favicons off, and this guarantees the arrow tips
# survive it.
CONTENT_RADIUS = 0.46

# Tab-icon zoom, in two tiers. Below ~48px the arrows collapse into grey noise,
# so 16/32 crop straight past them and let the face fill the circle; 48 and up
# show the whole logo. Nothing sits in between, because a half-cut arrowhead
# reads as a mistake rather than a crop. The full-logo tier can't exceed
# 0.5 / CONTENT_RADIUS = 1.087 or the arrow tips push outside the circle.
#
# Note the big sizes are zoomed too, not just the small ones: Google Search
# downscales whichever favicon it picks, so framing 16px tightly achieves
# nothing if the 96px file still has the panda floating in padding.
FAVICON_ZOOM = {16: 1.55, 32: 1.34}
FAVICON_ZOOM_FULL = 1.05

# Home-screen icons have square corners to spare, but the arrows span the full
# width, so this stays close to 1 — past ~1.1 the tips run off the edge.
PWA_ZOOM = 1.02

# Maskable icons must sit inside Android's safe zone — a circle covering 80% of
# the icon. At this zoom the artwork's enclosing circle spans 77% of the width.
MASKABLE_ZOOM = 0.84

SS = 4  # supersample the shape masks for clean anti-aliased edges


def _masks(img):
    """(cream, dark) boolean masks. The page background is neutral white; the
    logo's field is cream (blue channel well below red) and its linework is dark."""
    import numpy as np

    a = np.asarray(img.convert('RGB')).astype(int)
    r, g, b = a[:, :, 0], a[:, :, 1], a[:, :, 2]
    return (r - b > 8) & (r > 200), (r < 180) & (g < 180) & (b < 180)


def _find_logo(img):
    """Bbox of the largest logo blob — ignores mockups on a presentation sheet."""
    import numpy as np

    cream, dark = _masks(img)
    mask = cream | dark

    # Connected-component labelling on a downscaled copy: accurate enough to pick
    # the biggest blob, and fast without pulling in scipy.
    H, W = mask.shape
    step = max(1, max(H, W) // 400)
    small = mask[::step, ::step]
    sh, sw = small.shape

    seen = np.zeros((sh, sw), dtype=bool)
    best = None
    for sy in range(sh):
        for sx in range(sw):
            if not small[sy, sx] or seen[sy, sx]:
                continue
            q = deque([(sy, sx)])
            seen[sy, sx] = True
            area, y0, y1, x0, x1 = 0, sy, sy, sx, sx
            while q:
                cy, cx = q.popleft()
                area += 1
                y0, y1 = min(y0, cy), max(y1, cy)
                x0, x1 = min(x0, cx), max(x1, cx)
                for ny, nx in ((cy - 1, cx), (cy + 1, cx), (cy, cx - 1), (cy, cx + 1)):
                    if 0 <= ny < sh and 0 <= nx < sw and small[ny, nx] and not seen[ny, nx]:
                        seen[ny, nx] = True
                        q.append((ny, nx))
            if best is None or area > best[0]:
                best = (area, y0, y1, x0, x1)

    if best is None:
        raise CommandError('No logo artwork found in the source image.')

    _, y0, y1, x0, x1 = best
    return (max(0, x0 * step - step), max(0, y0 * step - step),
            min(W, (x1 + 1) * step + step), min(H, (y1 + 1) * step + step))


def _content(img, logo_box):
    """Bbox of the linework inside the logo, plus the radius of the smallest
    circle around it. That radius — not the bounding box — is what has to fit in
    a circular icon, and for this logo the two are within 3% of each other."""
    import numpy as np

    _, dark = _masks(img)
    x0, y0, x1, y1 = logo_box
    region = dark[y0:y1, x0:x1]
    ys, xs = np.nonzero(region)
    if len(xs) == 0:
        raise CommandError('No linework found inside the logo.')

    bx0, bx1, by0, by1 = xs.min(), xs.max(), ys.min(), ys.max()
    cx, cy = (bx0 + bx1) / 2, (by0 + by1) / 2
    radius = float(np.sqrt((xs - cx) ** 2 + (ys - cy) ** 2).max())
    return (x0 + bx0, y0 + by0, x0 + bx1 + 1, y0 + by1 + 1), radius


def _tile_color(img, logo_box):
    """The logo's own field colour — median of its cream pixels."""
    import numpy as np

    cream, dark = _masks(img)
    x0, y0, x1, y1 = logo_box
    a = np.asarray(img.convert('RGB'))[y0:y1, x0:x1]
    sel = cream[y0:y1, x0:x1] & ~dark[y0:y1, x0:x1]
    return tuple(int(v) for v in np.median(a[sel], axis=0))


def _master(img, logo_box, content_box, radius, fill):
    """A square cream canvas holding the linework at the target scale.

    Everything downstream is a resize of this, so the artwork keeps one
    consistent size relative to the icon edge no matter which shape is applied.
    """
    from PIL import Image
    import numpy as np

    x0, y0, x1, y1 = content_box
    crop = np.asarray(img.convert('RGB').crop(content_box)).copy()

    # The linework's bounding box pokes out past the logo's circle at the
    # corners, so the crop caught slivers of the white page behind it. Circular
    # icons mask those away, but square ones would show white notches — repaint
    # anything outside the circle in the logo's own cream. Positional rather than
    # colour-based, so the white glints in the panda's eyes survive.
    lx0, ly0, lx1, ly1 = logo_box
    lcx, lcy = (lx0 + lx1) / 2, (ly0 + ly1) / 2
    lr = min(lx1 - lx0, ly1 - ly0) / 2
    if _is_round(img, logo_box):
        yy, xx = np.mgrid[y0:y1, x0:x1]
        crop[((yy - lcy) ** 2 + (xx - lcx) ** 2) > (lr * 0.985) ** 2] = fill

    # CONTENT_RADIUS is a fraction of the icon's half-width, so the icon side is
    # the enclosing radius divided by it — not the diameter.
    side = int(round(radius / CONTENT_RADIUS))
    canvas = Image.new('RGB', (side, side), fill)
    canvas.paste(Image.fromarray(crop), ((side - (x1 - x0)) // 2, (side - (y1 - y0)) // 2))
    return canvas


def _is_round(img, logo_box):
    """True when the logo blob is a disc (a disc fills ~pi/4 of its bounding box)."""
    cream, dark = _masks(img)
    x0, y0, x1, y1 = logo_box
    filled = (cream | dark)[y0:y1, x0:x1]
    return abs(filled.mean() - 0.785) < 0.12


def _shape_mask(size, shape):
    """Anti-aliased alpha mask: a true circle, or a rounded square."""
    from PIL import Image, ImageDraw

    px = size * SS
    m = Image.new('L', (px, px), 0)
    d = ImageDraw.Draw(m)
    if shape == 'circle':
        d.ellipse([0, 0, px - 1, px - 1], fill=255)
    else:
        d.rounded_rectangle([0, 0, px - 1, px - 1], radius=round(px * 0.22), fill=255)
    return m.resize((size, size), Image.LANCZOS)


def _render(master, fill, size, zoom=1.0, shape='circle'):
    """One icon: the artwork scaled by `zoom` on a `size` tile of `fill`."""
    from PIL import Image

    art = master.resize((max(1, round(size * zoom)),) * 2, Image.LANCZOS)
    tile = Image.new('RGB', (size, size), fill)
    off = (size - art.width) // 2
    tile.paste(art, (off, off))

    if shape == 'square':
        return tile
    out = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    out.paste(tile, (0, 0), _shape_mask(size, shape))
    return out


def _save(img, path):
    """Write a PNG, palette-quantising the big ones.

    The logo is flat linework over one cream field, so 256 colours is visually
    lossless while cutting the 512px icon from ~250KB to ~20KB — worth it for an
    asset every visitor downloads.
    """
    from PIL import Image

    if min(img.size) >= 96:
        img = img.quantize(colors=256, method=Image.FASTOCTREE, dither=Image.NONE)
    img.save(path, optimize=True)


class Command(BaseCommand):
    help = "Regenerate favicons and PWA icons from the master Powerty logo."

    def add_arguments(self, parser):
        parser.add_argument(
            '--source', default=DEFAULT_SOURCE,
            help=f'Logo image, relative to static/ (default: {DEFAULT_SOURCE})',
        )

    def handle(self, *args, **options):
        try:
            from PIL import Image
            import numpy  # noqa: F401
        except ImportError:
            raise CommandError('Pillow and numpy are required: pip install Pillow numpy')

        root = Path(settings.BASE_DIR) / 'static'
        src = root / options['source']
        if not src.exists():
            raise CommandError(f'Source image not found: {src}')

        img = Image.open(src)
        logo_box = _find_logo(img)
        content_box, radius = _content(img, logo_box)
        fill = _tile_color(img, logo_box)
        master = _master(img, logo_box, content_box, radius, fill)

        cw, ch = content_box[2] - content_box[0], content_box[3] - content_box[1]
        self.stdout.write(
            f'  source {options["source"]}: logo {logo_box[2] - logo_box[0]}x'
            f'{logo_box[3] - logo_box[1]}px, linework {cw}x{ch}px, '
            f'field #{"%02x%02x%02x" % fill} — artwork spans '
            f'{cw / master.width:.0%} of the icon'
        )

        fav = root / 'favicon'
        icons = root / 'icons'
        fav.mkdir(parents=True, exist_ok=True)
        icons.mkdir(parents=True, exist_ok=True)
        written = []

        def zoom_for(size):
            return FAVICON_ZOOM.get(size, FAVICON_ZOOM_FULL)

        # Browser tab / Google results — a true circle, matching the logo's own
        # shape and the circular crop search engines apply anyway.
        for size in (16, 32, 48, 96):
            p = fav / f'favicon-{size}x{size}.png'
            _save(_render(master, fill, size, zoom_for(size)), p)
            written.append(p)

        ico = fav / 'favicon.ico'
        ico_sizes = (16, 32, 48, 64)
        frames = [_render(master, fill, s, zoom_for(s)).convert('RGBA') for s in ico_sizes]
        # Save from the largest frame — Pillow silently drops any requested size
        # bigger than the base image — and hand it the rest via append_images so
        # each frame keeps its own zoom instead of being downscaled from one image.
        frames[-1].save(ico, format='ICO', sizes=[(s, s) for s in ico_sizes],
                        append_images=frames[:-1])
        written.append(ico)

        # iOS home screen: must be opaque and square — iOS applies its own mask,
        # and any transparency it finds turns black.
        apple = fav / 'apple-touch-icon.png'
        _save(_render(master, fill, 180, shape='square'), apple)
        written.append(apple)

        # PWA / Android
        for size in (192, 512):
            p = icons / f'icon-{size}.png'
            _save(_render(master, fill, size, zoom=PWA_ZOOM, shape='round'), p)
            written.append(p)

            # Maskable: full-bleed, artwork inside the 80% safe zone so Android's
            # circular crop never clips it.
            m = icons / f'icon-maskable-{size}.png'
            _save(_render(master, fill, size, zoom=MASKABLE_ZOOM, shape='square'), m)
            written.append(m)

        for p in written:
            self.stdout.write(self.style.SUCCESS(f'  wrote {p.relative_to(root.parent)}'))
        self.stdout.write(self.style.SUCCESS(f'{len(written)} icons regenerated.'))
