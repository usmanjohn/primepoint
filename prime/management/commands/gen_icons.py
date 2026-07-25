"""Regenerate the whole Powerty icon set (favicons + PWA icons) from the master logo.

The source is `static/images/finlogo.png` — a presentation sheet where the big
circular panda logo on the left is the real high-resolution artwork and the small
tiles beside it are only mockups. This command finds that artwork automatically,
trims the page background off it, and renders every size the site ships so the
browser tab, the iOS home screen and the installed Android app all match.

    python manage.py gen_icons
    python manage.py gen_icons --source static/images/other_logo.png

Dev-only helper — the generated PNG/ICO files are committed to the repo, so
production never needs to run this.
"""

from collections import deque
from pathlib import Path

from django.conf import settings
from django.core.management.base import BaseCommand, CommandError

DEFAULT_SOURCE = 'images/finlogo.png'

# Tiny favicons: the two swoosh arrows collapse into noise below ~64px, so zoom
# past them and let the panda's head fill the tile instead. The smaller the icon,
# the tighter the crop — at 16px only the face survives, and that is the point.
SMALL_ZOOM = {16: 1.70, 32: 1.45, 48: 1.25}

SS = 2  # supersample the rounded-corner mask for clean edges


def _find_artwork(img):
    """Return the bbox of the largest logo blob on the sheet.

    The page background is near-white; the logo tile is cream and the linework is
    dark, so anything that is *not* neutral white belongs to some logo. The sheet
    holds several of those (master + mockups), and the biggest one is the master.
    """
    import numpy as np

    a = np.asarray(img.convert('RGB')).astype(int)
    r, g, b = a[:, :, 0], a[:, :, 1], a[:, :, 2]
    cream = (r - b > 8) & (r > 200)
    dark = (r < 180) & (g < 180) & (b < 180)
    mask = cream | dark

    # Label connected components on a downscaled copy — plenty accurate for
    # picking the biggest blob, and fast without scipy.
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
            area = 0
            y0 = y1 = sy
            x0 = x1 = sx
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
    # Back to full resolution, padded by one step to recover the blurred edge.
    return (
        max(0, x0 * step - step),
        max(0, y0 * step - step),
        min(W, (x1 + 1) * step + step),
        min(H, (y1 + 1) * step + step),
    )


def _tile_color(img, box):
    """The logo's own background colour, sampled just inside its top edge."""
    import numpy as np

    x0, y0, x1, y1 = box
    strip = np.asarray(img.convert('RGB').crop(
        (x0 + (x1 - x0) // 3, y0 + (y1 - y0) // 5, x1 - (x1 - x0) // 3, y0 + (y1 - y0) // 5 + 6)
    ))
    return tuple(int(v) for v in np.median(strip.reshape(-1, 3), axis=0))


def _master(img, box, fill):
    """Crop the artwork to a square and flatten the page background into `fill`.

    The master logo is a circle sitting on the white sheet, so the square crop has
    white corners and a soft drop shadow around the rim. Both get repainted in the
    logo's own cream, which makes the artwork tile seamlessly at any size.
    """
    from PIL import Image
    import numpy as np

    x0, y0, x1, y1 = box
    w, h = x1 - x0, y1 - y0
    side = max(w, h)
    cx, cy = (x0 + x1) // 2, (y0 + y1) // 2

    canvas = Image.new('RGB', (side, side), fill)
    canvas.paste(img.convert('RGB').crop(box), ((side - w) // 2, (side - h) // 2))

    # Is the blob round? (a disc covers ~pi/4 of its bounding box)
    a = np.asarray(img.convert('RGB').crop(box)).astype(int)
    r, g, b = a[:, :, 0], a[:, :, 1], a[:, :, 2]
    filled = ((r - b > 8) & (r > 200)) | ((r < 180) & (g < 180) & (b < 180))
    if abs(filled.mean() - 0.785) < 0.12:
        yy, xx = np.mgrid[0:side, 0:side]
        c = (side - 1) / 2
        # Bite in slightly past the rim so the drop shadow goes with the corners.
        outside = ((yy - c) ** 2 + (xx - c) ** 2) > (side * 0.478) ** 2
        arr = np.asarray(canvas).copy()
        arr[outside] = fill
        canvas = Image.fromarray(arr)

    return canvas


def _save(img, path):
    """Write a PNG, palette-quantising the big ones.

    The logo is flat linework over one cream field, so 256 colours is visually
    lossless while cutting the 512px icon from ~250KB to ~50KB — worth it for an
    asset every visitor downloads.
    """
    from PIL import Image

    if min(img.size) >= 96:
        img = img.quantize(colors=256, method=Image.FASTOCTREE, dither=Image.NONE)
    img.save(path, optimize=True)


def _round_mask(size, radius_ratio):
    from PIL import Image, ImageDraw

    px = size * SS
    m = Image.new('L', (px, px), 0)
    ImageDraw.Draw(m).rounded_rectangle(
        [0, 0, px - 1, px - 1], radius=round(px * radius_ratio), fill=255
    )
    return m.resize((size, size), Image.LANCZOS)


def _render(master, fill, size, zoom=1.0, radius_ratio=0.22, opaque=False):
    """One icon: the artwork scaled by `zoom` on a `size` square of `fill`."""
    from PIL import Image

    art = master.resize((max(1, round(size * zoom)),) * 2, Image.LANCZOS)
    tile = Image.new('RGB', (size, size), fill)
    off = (size - art.width) // 2
    tile.paste(art, (off, off))

    if opaque or radius_ratio <= 0:
        return tile
    out = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    out.paste(tile, (0, 0), _round_mask(size, radius_ratio))
    return out


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
        box = _find_artwork(img)
        fill = _tile_color(img, box)
        master = _master(img, box, fill)

        self.stdout.write(
            f'  source {options["source"]} — artwork {box[2] - box[0]}x{box[3] - box[1]}px '
            f'at ({box[0]},{box[1]}), tile colour #{"%02x%02x%02x" % fill}'
        )

        fav = root / 'favicon'
        icons = root / 'icons'
        fav.mkdir(parents=True, exist_ok=True)
        icons.mkdir(parents=True, exist_ok=True)
        written = []

        def zoom_for(size):
            return SMALL_ZOOM.get(size, 1.0)

        # Browser tab
        for size in (16, 32, 48, 96):
            p = fav / f'favicon-{size}x{size}.png'
            _save(_render(master, fill, size, zoom_for(size), radius_ratio=0.18), p)
            written.append(p)

        # Multi-resolution .ico — each frame rendered at its own zoom, so the
        # 16px frame is the tight crop rather than a squashed 256px one.
        ico = fav / 'favicon.ico'
        ico_sizes = (16, 32, 48, 64)
        frames = [_render(master, fill, s, zoom_for(s), radius_ratio=0.18).convert('RGBA')
                  for s in ico_sizes]
        # Save from the largest frame — Pillow silently drops any requested size
        # bigger than the base image — and hand it the rest via append_images so
        # each frame keeps its own zoom instead of being downscaled from 256px.
        frames[-1].save(ico, format='ICO', sizes=[(s, s) for s in ico_sizes],
                        append_images=frames[:-1])
        written.append(ico)

        # iOS home screen — must be opaque; iOS rounds the corners itself.
        apple = fav / 'apple-touch-icon.png'
        _save(_render(master, fill, 180, opaque=True), apple)
        written.append(apple)

        # PWA / Android
        for size in (192, 512):
            p = icons / f'icon-{size}.png'
            _save(_render(master, fill, size), p)
            written.append(p)

            # Maskable: full-bleed, artwork kept inside the 80% safe zone so
            # Android's circular crop never clips it.
            m = icons / f'icon-maskable-{size}.png'
            _save(_render(master, fill, size, zoom=0.76, opaque=True), m)
            written.append(m)

        for p in written:
            self.stdout.write(self.style.SUCCESS(f'  wrote {p.relative_to(root.parent)}'))
        self.stdout.write(self.style.SUCCESS(f'{len(written)} icons regenerated.'))
