"""Tiny BPMN layout kit -> native Visio (.vsdx) + SVG preview.

One model, two backends, so the PDF you read and the Visio file you edit
are always the same picture. Units are millimetres, origin top-left.
No masters, no stencils: every element is a plain Visio shape with its
own geometry, so it opens in any Visio 2013+ and stays editable.
"""
import math
import zipfile
from xml.sax.saxutils import escape

MM = 1 / 25.4  # mm -> inch (Visio's internal unit)

# ---------------------------------------------------------------- colours
C = {
    'ink': '#1F2937', 'line': '#374151', 'muted': '#6B7280',
    'task': '#FFFFFF', 'task_ln': '#1F2937',
    'start': '#4CAF50', 'end': '#E53935', 'timer': '#F6B73C',
    'msg': '#4C8BF5', 'gate': '#FFF8E1', 'data': '#FFFFFF',
    'lanehd': '#D9DEE5', 'poolhd': '#BFC7D2', 'lane': '#FFFFFF',
    'red': '#C00000', 'note': '#555555', 'group': '#F4F7FB',
    'store': '#E8F0FE', 'proc': '#EEF6EE',
}


# ================================================================ shapes
class Shape:
    """A Visio shape: bbox + geometry paths + optional rich text."""

    def __init__(self, x, y, w, h, geoms=(), fill=None, stroke=C['line'],
                 sw=0.25, dash=0, rounding=0, runs=None, size=7, bold=False,
                 italic=False, color=C['ink'], halign='center', valign='middle',
                 textbox=None, rotate=False, end_arrow=False, margin=1.2):
        self.x, self.y, self.w, self.h = x, y, w, h
        self.geoms = list(geoms)      # [('poly', pts, closed) | ('ell', cx, cy, rx, ry)]
        self.fill, self.stroke, self.sw = fill, stroke, sw
        self.dash, self.rounding = dash, rounding
        if isinstance(runs, str):
            runs = [(runs, bold, italic, color)]
        self.runs = runs or []
        self.size, self.halign, self.valign = size, halign, valign
        self.textbox = textbox        # (dx, dy, w, h) relative to bbox top-left
        self.rotate = rotate
        self.end_arrow = end_arrow
        self.margin = margin


def rect_geom(w, h):
    return ('poly', [(0, 0), (w, 0), (w, h), (0, h)], True)


def box(x, y, w, h, text='', **kw):
    return Shape(x, y, w, h, [rect_geom(w, h)], **kw)


def text(x, y, w, h, t, **kw):
    kw.setdefault('stroke', None)
    return Shape(x, y, w, h, [], runs=t, **kw)


def line(points, dash=0, arrow=True, sw=0.3, stroke=C['line']):
    xs = [p[0] for p in points]
    ys = [p[1] for p in points]
    x0, y0 = min(xs), min(ys)
    w, h = max(max(xs) - x0, 0.01), max(max(ys) - y0, 0.01)
    rel = [(px - x0, py - y0) for px, py in points]
    return Shape(x0, y0, w, h, [('poly', rel, False)], fill=None, stroke=stroke,
                 sw=sw, dash=dash, end_arrow=arrow)


# ================================================================ backends
def _hex(c):
    return c


def svg_page(shapes, W, H):
    out = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}mm" height="{H}mm" '
           f'viewBox="0 0 {W} {H}" font-family="Calibri, Carlito, Arial, sans-serif">',
           '<defs><marker id="ar" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="5" '
           'markerHeight="5" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" '
           f'fill="{C["line"]}"/></marker></defs>',
           f'<rect x="0" y="0" width="{W}" height="{H}" fill="#fff"/>',
           '<g transform="scale(0.1)">']
    import copy
    K = 10
    for s0 in shapes:
        s = copy.copy(s0)
        s.x, s.y, s.w, s.h = s0.x * K, s0.y * K, s0.w * K, s0.h * K
        s.sw, s.rounding, s.margin, s.size = s0.sw * K, s0.rounding * K, s0.margin * K, s0.size * K
        s.textbox = tuple(v * K for v in s0.textbox) if s0.textbox else None
        s.geoms = [(g0[0], [(a * K, b * K) for a, b in g0[1]], g0[2]) if g0[0] == 'poly'
                   else ('ell',) + tuple(v * K for v in g0[1:]) for g0 in s0.geoms]
        g = []
        st = (f'stroke="{s.stroke}" stroke-width="{s.sw}"' if s.stroke else 'stroke="none"')
        if s.dash == 2:
            st += ' stroke-dasharray="22,14"'
        elif s.dash == 3:
            st += ' stroke-dasharray="6,10"'
        for gm in s.geoms:
            if gm[0] == 'poly':
                pts, closed = gm[1], gm[2]
                if closed and s.rounding and len(pts) == 4 and pts[0] == (0, 0):
                    g.append(f'<rect x="{s.x}" y="{s.y}" width="{s.w}" height="{s.h}" '
                             f'rx="{s.rounding}" fill="{s.fill or "none"}" {st}/>')
                    continue
                d = ' '.join(f'{s.x + px:.2f},{s.y + py:.2f}' for px, py in pts)
                if closed:
                    g.append(f'<polygon points="{d}" fill="{s.fill or "none"}" {st}/>')
                else:
                    mk = ' marker-end="url(#ar)"' if s.end_arrow else ''
                    g.append(f'<polyline points="{d}" fill="none" {st}{mk}/>')
            else:
                _, cx, cy, rx, ry = gm
                g.append(f'<ellipse cx="{s.x + cx}" cy="{s.y + cy}" rx="{rx}" ry="{ry}" '
                         f'fill="{s.fill or "none"}" {st}/>')
        if s.runs:
            tx, ty, tw, th = (s.textbox or (0, 0, s.w, s.h))
            tx += s.x
            ty += s.y
            jc = {'top': 'flex-start', 'middle': 'center', 'bottom': 'flex-end'}[s.valign]
            ta = {'left': 'left', 'center': 'center', 'right': 'right'}[s.halign]
            spans = ''.join(
                f'<span style="font-weight:{700 if b else 400};font-style:{"italic" if i else "normal"};'
                f'color:{c}">{escape(t)}</span>' for t, b, i, c in s.runs)
            fs = s.size * 0.3528
            inner = (f'<div xmlns="http://www.w3.org/1999/xhtml" style="width:100%;height:100%;'
                     f'display:flex;flex-direction:column;justify-content:{jc};box-sizing:border-box;'
                     f'padding:{s.margin}px;font-size:{fs:.3f}px;line-height:1.15;text-align:{ta};'
                     f'white-space:pre-wrap;overflow-wrap:break-word;color:{C["ink"]}"><div>{spans}</div></div>')
            if s.rotate:  # vertical lane label, reads bottom-to-top
                cx, cy = tx + tw / 2, ty + th / 2
                g.append(f'<g transform="rotate(-90 {cx} {cy})"><foreignObject x="{cx - th / 2}" '
                         f'y="{cy - tw / 2}" width="{th}" height="{tw}">{inner}</foreignObject></g>')
            else:
                g.append(f'<foreignObject x="{tx}" y="{ty}" width="{tw}" height="{th}">{inner}</foreignObject>')
        out.extend(g)
    out.append('</g></svg>')
    return '\n'.join(out)


def _cell(n, v, u=None):
    u = f' U="{u}"' if u else ''
    return f'<Cell N="{n}" V="{v}"{u}/>'


def _vsdx_shape(s, sid, H):
    i = lambda mm: f'{mm * MM:.5f}'
    w, h = s.w, s.h
    cells = [
        _cell('PinX', i(s.x + w / 2)), _cell('PinY', i(H - (s.y + h / 2))),
        _cell('Width', i(w)), _cell('Height', i(h)),
        _cell('LocPinX', i(w / 2)), _cell('LocPinY', i(h / 2)),
        _cell('Angle', 0), _cell('FlipX', 0), _cell('FlipY', 0),
        _cell('LineWeight', i(s.sw)),
        _cell('LineColor', s.stroke or '#000000'),
        _cell('LinePattern', (0 if not s.stroke else (s.dash or 1))),
        _cell('FillForegnd', s.fill or '#FFFFFF'),
        _cell('FillPattern', 1 if s.fill else 0),
        _cell('Rounding', i(s.rounding)),
        _cell('LeftMargin', i(s.margin * 0.35)), _cell('RightMargin', i(s.margin * 0.35)),
        _cell('TopMargin', i(s.margin * 0.35)), _cell('BottomMargin', i(s.margin * 0.35)),
        _cell('VerticalAlign', {'top': 0, 'middle': 1, 'bottom': 2}[s.valign]),
    ]
    if s.end_arrow:
        cells += [_cell('EndArrow', 4), _cell('EndArrowSize', 1)]
    if s.runs and (s.textbox or s.rotate):
        tx, ty, tw, th = s.textbox or (0, 0, w, h)
        if s.rotate:
            cells += [_cell('TxtPinX', i(tx + tw / 2)), _cell('TxtPinY', i(h - (ty + th / 2))),
                      _cell('TxtWidth', i(th)), _cell('TxtHeight', i(tw)),
                      _cell('TxtLocPinX', i(th / 2)), _cell('TxtLocPinY', i(tw / 2)),
                      _cell('TxtAngle', f'{math.pi / 2:.6f}')]
        else:
            cells += [_cell('TxtPinX', i(tx + tw / 2)), _cell('TxtPinY', i(h - (ty + th / 2))),
                      _cell('TxtWidth', i(tw)), _cell('TxtHeight', i(th)),
                      _cell('TxtLocPinX', i(tw / 2)), _cell('TxtLocPinY', i(th / 2))]
    secs = []
    if s.runs:
        styles = []
        for t, b, it, c in s.runs:
            key = (b, it, c)
            if key not in styles:
                styles.append(key)
        rows = ''.join(
            f'<Row IX="{k}">{_cell("Size", f"{s.size / 72:.5f}", "PT")}'
            f'{_cell("Style", (1 if b else 0) | (2 if it else 0))}{_cell("Color", c)}</Row>'
            for k, (b, it, c) in enumerate(styles))
        secs.append(f'<Section N="Character">{rows}</Section>')
        secs.append(f'<Section N="Paragraph"><Row IX="0">'
                    f'{_cell("HorzAlign", {"left": 0, "center": 1, "right": 2}[s.halign])}'
                    f'{_cell("SpLine", "-1.15")}</Row></Section>')
    for gi, gm in enumerate(s.geoms):
        nofill = 1 if (not s.fill or (gm[0] == 'poly' and not gm[2])) else 0
        rows = [_cell('NoFill', nofill), _cell('NoLine', 0 if s.stroke else 1),
                _cell('NoShow', 0), _cell('NoSnap', 0)]
        if gm[0] == 'poly':
            pts, closed = gm[1], gm[2]
            if closed:
                pts = list(pts) + [pts[0]]
            for k, (px, py) in enumerate(pts):
                t = 'MoveTo' if k == 0 else 'LineTo'
                rows.append(f'<Row T="{t}" IX="{k + 1}">{_cell("X", i(px))}{_cell("Y", i(h - py))}</Row>')
        else:
            _, cx, cy, rx, ry = gm
            rows.append(f'<Row T="Ellipse" IX="1">{_cell("X", i(cx))}{_cell("Y", i(h - cy))}'
                        f'{_cell("A", i(cx + rx))}{_cell("B", i(h - cy))}'
                        f'{_cell("C", i(cx))}{_cell("D", i(h - cy - ry))}</Row>')
        secs.append(f'<Section N="Geometry" IX="{gi}">{"".join(rows)}</Section>')
    txt = ''
    if s.runs:
        styles = []
        parts = []
        for t, b, it, c in s.runs:
            key = (b, it, c)
            if key not in styles:
                styles.append(key)
            parts.append(f'<cp IX="{styles.index(key)}"/>{escape(t)}')
        txt = f'<Text>{"".join(parts)}</Text>'
    return (f'<Shape ID="{sid}" Type="Shape" LineStyle="0" FillStyle="0" TextStyle="0">'
            f'{"".join(cells)}{"".join(secs)}{txt}</Shape>')


NS = 'http://schemas.microsoft.com/office/visio/2012/main'
RNS = 'http://schemas.openxmlformats.org/officeDocument/2006/relationships'
VREL = 'http://schemas.microsoft.com/visio/2010/relationships'


def write_vsdx(path, pages, title='BPMN', author=''):
    """pages: list of (name, W, H, shapes)."""
    z = zipfile.ZipFile(path, 'w', zipfile.ZIP_DEFLATED)
    ct = ['<?xml version="1.0" encoding="UTF-8" standalone="yes"?>',
          '<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">',
          '<Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>',
          '<Default Extension="xml" ContentType="application/xml"/>',
          '<Override PartName="/visio/document.xml" ContentType="application/vnd.ms-visio.drawing.main+xml"/>',
          '<Override PartName="/visio/pages/pages.xml" ContentType="application/vnd.ms-visio.pages+xml"/>',
          '<Override PartName="/visio/windows.xml" ContentType="application/vnd.ms-visio.windows+xml"/>',
          '<Override PartName="/docProps/core.xml" ContentType="application/vnd.openxmlformats-package.core-properties+xml"/>',
          '<Override PartName="/docProps/app.xml" ContentType="application/vnd.openxmlformats-officedocument.extended-properties+xml"/>']
    for k in range(len(pages)):
        ct.append(f'<Override PartName="/visio/pages/page{k + 1}.xml" ContentType="application/vnd.ms-visio.page+xml"/>')
    ct.append('</Types>')
    z.writestr('[Content_Types].xml', '\n'.join(ct))
    z.writestr('_rels/.rels',
               '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
               '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
               f'<Relationship Id="rId1" Type="{VREL}/document" Target="visio/document.xml"/>'
               '<Relationship Id="rId2" Type="http://schemas.openxmlformats.org/package/2006/relationships/metadata/core-properties" Target="docProps/core.xml"/>'
               '<Relationship Id="rId3" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/extended-properties" Target="docProps/app.xml"/>'
               '</Relationships>')
    z.writestr('docProps/core.xml',
               '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
               '<cp:coreProperties xmlns:cp="http://schemas.openxmlformats.org/package/2006/metadata/core-properties" '
               'xmlns:dc="http://purl.org/dc/elements/1.1/"><dc:title>' + escape(title) +
               '</dc:title><dc:creator>' + escape(author) + '</dc:creator></cp:coreProperties>')
    z.writestr('docProps/app.xml',
               '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
               '<Properties xmlns="http://schemas.openxmlformats.org/officeDocument/2006/extended-properties">'
               '<Application>Microsoft Visio</Application></Properties>')
    style0 = ''.join([
        _cell('EnableLineProps', 1), _cell('EnableFillProps', 1), _cell('EnableTextProps', 1),
        _cell('HideForApply', 0), _cell('LineWeight', '0.01041666666666667'), _cell('LineColor', '#000000'),
        _cell('LinePattern', 1), _cell('Rounding', 0), _cell('EndArrowSize', 2), _cell('BeginArrow', 0),
        _cell('EndArrow', 0), _cell('LineCap', 0), _cell('BeginArrowSize', 2), _cell('LineColorTrans', 0),
        _cell('FillForegnd', '#FFFFFF'), _cell('FillBkgnd', '#FFFFFF'), _cell('FillPattern', 1),
        _cell('ShdwForegnd', '#000000'), _cell('ShdwPattern', 0), _cell('FillForegndTrans', 0),
        _cell('FillBkgndTrans', 0), _cell('ShdwForegndTrans', 0),
        _cell('LeftMargin', 0), _cell('RightMargin', 0), _cell('TopMargin', 0), _cell('BottomMargin', 0),
        _cell('VerticalAlign', 1), _cell('TextBkgnd', 0), _cell('DefaultTabStop', 0.5),
        _cell('TextDirection', 0), _cell('TextBkgndTrans', 0),
        '<Section N="Character"><Row IX="0">', _cell('Font', 'Calibri'), _cell('Color', '#000000'),
        _cell('Style', 0), _cell('Case', 0), _cell('Pos', 0), _cell('FontScale', 1),
        _cell('Size', '0.1111111111111111'), _cell('DblUnderline', 0), _cell('Overline', 0),
        _cell('Strikethru', 0), _cell('Letterspace', 0), _cell('ColorTrans', 0), '</Row></Section>',
        '<Section N="Paragraph"><Row IX="0">', _cell('IndFirst', 0), _cell('IndLeft', 0), _cell('IndRight', 0),
        _cell('SpLine', -1.2), _cell('SpBefore', 0), _cell('SpAfter', 0), _cell('HorzAlign', 1),
        _cell('Bullet', 0), '</Row></Section>'])
    z.writestr('visio/document.xml',
               f'<?xml version="1.0" encoding="UTF-8" standalone="yes"?><VisioDocument xmlns="{NS}" xmlns:r="{RNS}" xml:space="preserve">'
               '<DocumentSettings TopPage="0" DefaultTextStyle="0" DefaultLineStyle="0" DefaultFillStyle="0" DefaultGuideStyle="0">'
               '<GlueSettings>9</GlueSettings><SnapSettings>65847</SnapSettings><SnapExtensions>34</SnapExtensions>'
               '<SnapAngles/><DynamicGridEnabled>1</DynamicGridEnabled><ProtectStyles>0</ProtectStyles>'
               '<ProtectShapes>0</ProtectShapes><ProtectMasters>0</ProtectMasters><ProtectBkgnds>0</ProtectBkgnds>'
               '</DocumentSettings>'
               '<Colors><ColorEntry IX="0" RGB="#000000"/><ColorEntry IX="1" RGB="#FFFFFF"/></Colors>'
               '<FaceNames><FaceName NameU="Calibri" UnicodeRanges="-536859905 -1073732485 9 0" CharSets="536871423 0" Panose="2 15 5 2 2 2 4 3 2 4" Flags="325"/></FaceNames>'
               f'<StyleSheets><StyleSheet ID="0" NameU="No Style" IsCustomNameU="1" Name="No Style" IsCustomName="1">{style0}</StyleSheet></StyleSheets>'
               '</VisioDocument>')
    z.writestr('visio/_rels/document.xml.rels',
               '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
               '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
               f'<Relationship Id="rId1" Type="{VREL}/pages" Target="pages/pages.xml"/>'
               f'<Relationship Id="rId2" Type="{VREL}/windows" Target="windows.xml"/>'
               '</Relationships>')
    z.writestr('visio/windows.xml',
               f'<?xml version="1.0" encoding="UTF-8" standalone="yes"?><Windows ClientWidth="1600" ClientHeight="900" xmlns="{NS}" xmlns:r="{RNS}" xml:space="preserve">'
               '<Window ID="0" WindowType="Drawing" WindowState="1073741824" WindowLeft="-8" WindowTop="-31" '
               'WindowWidth="1616" WindowHeight="939" ContainerType="Page" Page="0" ViewScale="-1" ViewCenterX="0" ViewCenterY="0">'
               '<ShowRulers>1</ShowRulers><ShowGrid>0</ShowGrid><ShowPageBreaks>0</ShowPageBreaks><ShowGuides>1</ShowGuides>'
               '<ShowConnectionPoints>1</ShowConnectionPoints><GlueSettings>9</GlueSettings><SnapSettings>65847</SnapSettings>'
               '<SnapExtensions>34</SnapExtensions><SnapAngles/><DynamicGridEnabled>1</DynamicGridEnabled>'
               '<TabSplitterPos>0.5</TabSplitterPos></Window></Windows>')
    pg = [f'<?xml version="1.0" encoding="UTF-8" standalone="yes"?><Pages xmlns="{NS}" xmlns:r="{RNS}" xml:space="preserve">']
    rels = ['<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
            '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">']
    for k, (name, W, H, shapes) in enumerate(pages):
        pg.append(f'<Page ID="{k}" NameU="{escape(name)}" Name="{escape(name)}" ViewScale="-1" ViewCenterX="0" ViewCenterY="0">'
                  f'<PageSheet LineStyle="0" FillStyle="0" TextStyle="0">'
                  f'{_cell("PageWidth", f"{W * MM:.5f}", "MM")}{_cell("PageHeight", f"{H * MM:.5f}", "MM")}'
                  f'{_cell("ShdwOffsetX", "0.1181102362204724")}{_cell("ShdwOffsetY", "-0.1181102362204724")}'
                  f'{_cell("PageScale", "0.03937007874015748", "MM")}{_cell("DrawingScale", "0.03937007874015748", "MM")}'
                  f'{_cell("DrawingSizeType", 0)}{_cell("DrawingScaleType", 0)}{_cell("InhibitSnap", 0)}'
                  f'{_cell("PrintPageOrientation", 2)}{_cell("PaperKind", 8)}'
                  f'</PageSheet><Rel r:id="rId{k + 1}"/></Page>')
        rels.append(f'<Relationship Id="rId{k + 1}" Type="{VREL}/page" Target="page{k + 1}.xml"/>')
        body = ''.join(_vsdx_shape(s, n + 1, H) for n, s in enumerate(shapes))
        z.writestr(f'visio/pages/page{k + 1}.xml',
                   f'<?xml version="1.0" encoding="UTF-8" standalone="yes"?><PageContents xmlns="{NS}" xmlns:r="{RNS}" xml:space="preserve">'
                   f'<Shapes>{body}</Shapes></PageContents>')
    pg.append('</Pages>')
    rels.append('</Relationships>')
    z.writestr('visio/pages/pages.xml', ''.join(pg))
    z.writestr('visio/pages/_rels/pages.xml.rels', ''.join(rels))
    z.close()


# ================================================================ BPMN layer
TW, TH = 32, 19      # task size
EV = 9               # event diameter
GW = 12              # gateway size
COLW = 43            # column pitch


class Diagram:
    """A BPMN 'As Is' sheet laid out like the bank's own template:
    passport / roles / terms boxes on top, then a pool of swimlanes."""

    def __init__(self, tab, passport, roles, terms, pool, lanes, ncols,
                 lane_h=44, head_h=30):
        self.tab = tab
        self.passport, self.roles, self.terms = passport, roles, terms
        self.pool = pool
        self.lanes = [(l, lane_h) if isinstance(l, str) else l for l in lanes]
        self.ncols = ncols
        self.head_h = head_h
        self.nodes = {}
        self.edges = []
        self.extra = []
        self.steps = []      # for the step register (xlsx)
        self.x0 = 10
        self.top = 10 + head_h + 8
        self.lane_x = self.x0 + 9 + 12
        self.W = max(self.lane_x + 14 + ncols * COLW + 8, 420)
        self.lane_y = []
        y = self.top
        for _, h in self.lanes:
            self.lane_y.append(y)
            y += h
        self.H = y + 10

    # ------------------------------------------------ placement
    def pos(self, lane, col, dy=0):
        ly = self.lane_y[lane]
        lh = self.lanes[lane][1]
        return self.lane_x + 14 + col * COLW + COLW / 2 - 6, ly + lh / 2 + dy

    def _add(self, nid, kind, cx, cy, w, h, label, lane):
        self.nodes[nid] = dict(kind=kind, cx=cx, cy=cy, w=w, h=h, label=label, lane=lane)

    def task(self, nid, lane, col, label, system='', dy=0, sub=False, note=None, note_dy=-18):
        cx, cy = self.pos(lane, col, dy)
        self._add(nid, 'task', cx, cy, TW, TH, label, lane)
        self.steps.append((label, self.lanes[lane][0], system, note or ''))
        if note:
            self.annotate(nid, note, dy=note_dy)
        if system:
            self.extra.append(text(cx - TW / 2 - 3, cy + TH / 2 + 0.3, TW + 6, 4.2,
                                   system, size=5.5, italic=True, color=C['muted']))
        self.nodes[nid]['sub'] = sub

    def event(self, nid, lane, col, kind, label, dy=0):
        cx, cy = self.pos(lane, col, dy)
        self._add(nid, kind, cx, cy, EV, EV, label, lane)

    def gate(self, nid, lane, col, label, kind='xor', dy=0, lpos='top'):
        cx, cy = self.pos(lane, col, dy)
        self._add(nid, 'gate_' + kind, cx, cy, GW, GW, label, lane)
        self.nodes[nid]['lpos'] = lpos

    def data(self, nid, lane, col, label, dx=0, dy=0):
        cx, cy = self.pos(lane, col, dy)
        self._add(nid, 'data', cx + dx, cy, 8, 10, label, lane)

    def annotate(self, nid, note, dy=-18, dx=-4, w=None):
        n = self.nodes[nid]
        w = w or TW + 8
        x = n['cx'] - n['w'] / 2 + dx
        lines = note.count('\n') + 1
        h = 3.2 * lines + 1.6
        y = n['cy'] + dy - h
        geo = [('poly', [(2, 0), (0, 0), (0, h), (2, h)], False)]
        self.extra.append(Shape(x, y, w, h, geo, stroke=C['note'], sw=0.25, runs=note,
                                size=5.3, color=C['note'], halign='left', margin=2.6))
        top = n['cy'] - n['h'] / 2
        self.extra.append(line([(x + 1.2, y + h), (n['cx'] - 2, top)], dash=3, arrow=False,
                               sw=0.25, stroke=C['note']))

    def flow(self, a, b, label='', route='auto', ry=None, rx=None, msg=False, exit=None, enter=None,
             assoc=False):
        self.edges.append(dict(a=a, b=b, label=label, route=route, ry=ry, rx=rx, msg=msg,
                               exit=exit, enter=enter, assoc=assoc))

    # ------------------------------------------------ routing
    @staticmethod
    def side(n, s):
        cx, cy, w, h = n['cx'], n['cy'], n['w'], n['h']
        return {'r': (cx + w / 2, cy), 'l': (cx - w / 2, cy),
                't': (cx, cy - h / 2), 'b': (cx, cy + h / 2)}[s]

    def _route(self, e):
        A, B = self.nodes[e['a']], self.nodes[e['b']]
        ax, ay, bx, by = A['cx'], A['cy'], B['cx'], B['cy']
        r = e['route']
        if r == 'over' or r == 'under':
            s = 't' if r == 'over' else 'b'
            p, q = self.side(A, e['exit'] or s), self.side(B, e['enter'] or s)
            yy = e['ry'] if e['ry'] is not None else (
                min(p[1], q[1]) - 7 if r == 'over' else max(p[1], q[1]) + 7)
            return [p, (p[0], yy), (q[0], yy), q]
        if r == 'vh':   # vertical first, then horizontal into the side
            s = e['exit'] or ('b' if by > ay else 't')
            p = self.side(A, s)
            q = self.side(B, e['enter'] or ('l' if bx > ax else 'r'))
            return [p, (p[0], q[1]), q]
        if r == 'hv':   # horizontal first, then vertical into top/bottom
            p = self.side(A, e['exit'] or ('r' if bx > ax else 'l'))
            q = self.side(B, e['enter'] or ('t' if by > ay else 'b'))
            return [p, (q[0], p[1]), q]
        # auto
        if abs(ay - by) < 0.5:
            if bx > ax:
                return [self.side(A, 'r'), self.side(B, 'l')]
            e2 = dict(e, route='over')
            return self._route(e2)
        if abs(ax - bx) < 0.5:
            if by > ay:
                return [self.side(A, 'b'), self.side(B, 't')]
            return [self.side(A, 't'), self.side(B, 'b')]
        if bx > ax:
            p, q = self.side(A, e['exit'] or 'r'), self.side(B, e['enter'] or 'l')
            if e['exit'] in ('b', 't'):
                return [p, (p[0], q[1]), q]
            xm = e['rx'] if e['rx'] is not None else q[0] - 6
            return [p, (xm, p[1]), (xm, q[1]), q]
        # backwards across lanes
        p = self.side(A, e['exit'] or ('t' if by < ay else 'b'))
        q = self.side(B, e['enter'] or 'r')
        if q[0] > B['cx']:   # entering right side: go up then left
            return [p, (p[0], q[1]), q]
        return [p, (p[0], q[1]), q]

    # ------------------------------------------------ rendering
    def _header(self):
        S = []
        y, h = 10, self.head_h
        W = self.W - 20
        w1, w2 = W * 0.31, W * 0.36
        w3 = W - w1 - w2 - 8
        runs = []
        for k, (lab, val) in enumerate(self.passport):
            runs += [(lab + ': ', True, False, C['ink']), (val + ('\n' if k < len(self.passport) - 1 else ''), False, False, C['ink'])]
        S.append(Shape(10, y, w1, h, [rect_geom(w1, h)], fill='#FFFFFF', stroke=C['ink'], sw=0.35,
                       rounding=2.5, runs=runs, size=8, halign='left', valign='top', margin=3))
        runs = [('Роли:\n', True, False, C['ink'])]
        for k, (lab, val) in enumerate(self.roles):
            runs += [('Роль «' + lab + '»', True, False, C['ink']),
                     (' – ' + val + ('\n' if k < len(self.roles) - 1 else ''), False, False, C['ink'])]
        S.append(Shape(10 + w1 + 4, y, w2, h, [rect_geom(w2, h)], fill='#FFFFFF', stroke=C['ink'],
                       sw=0.35, rounding=2.5, runs=runs, size=7.2, halign='left', valign='top', margin=3))
        runs = [('Используемые термины:\n', True, False, C['red'])]
        for k, (lab, val) in enumerate(self.terms):
            runs += [(lab + ' – ' + val + ('\n' if k < len(self.terms) - 1 else ''), False, False, C['red'])]
        S.append(Shape(10 + w1 + w2 + 8, y, w3, h, [rect_geom(w3, h)], fill='#FFFFFF', stroke=C['ink'],
                       sw=0.35, rounding=2.5, runs=runs, size=6.6, halign='left', valign='top', margin=3))
        return S

    def _pool(self):
        S = []
        ph = sum(h for _, h in self.lanes)
        pw = self.W - 10 - self.x0
        S.append(box(self.x0, self.top, pw, ph, fill=None, stroke=C['ink'], sw=0.5))
        S.append(Shape(self.x0, self.top, 9, ph, [rect_geom(9, ph)], fill=C['poolhd'], stroke=C['ink'],
                       sw=0.5, runs=self.pool, size=7.5, bold=True, rotate=True))
        for (lab, h), y in zip(self.lanes, self.lane_y):
            S.append(box(self.x0 + 9, y, pw - 9, h, fill=None, stroke=C['ink'], sw=0.35))
            S.append(Shape(self.x0 + 9, y, 12, h, [rect_geom(12, h)], fill=C['lanehd'], stroke=C['ink'],
                           sw=0.35, runs=lab, size=6.3, bold=True, rotate=True))
        return S

    def _node(self, n):
        x, y = n['cx'] - n['w'] / 2, n['cy'] - n['h'] / 2
        w, h, k, lab = n['w'], n['h'], n['kind'], n['label']
        lbl_below = (-11, h + 0.8, w + 22, 9)
        if k == 'task':
            geo = [rect_geom(w, h)]
            if n.get('sub'):
                geo += [('poly', [(w / 2 - 2, h - 4.5), (w / 2 + 2, h - 4.5), (w / 2 + 2, h - 0.5), (w / 2 - 2, h - 0.5)], True),
                        ('poly', [(w / 2 - 1.3, h - 2.5), (w / 2 + 1.3, h - 2.5)], False),
                        ('poly', [(w / 2, h - 3.8), (w / 2, h - 1.2)], False)]
                tb = (0, 0, w, h - 4)
            else:
                tb = None
            return Shape(x, y, w, h, geo, fill=C['task'], stroke=C['task_ln'], sw=0.35, rounding=2.2,
                         runs=lab, size=6.5, textbox=tb)
        if k == 'start':
            return Shape(x, y, w, h, [('ell', w / 2, h / 2, w / 2, h / 2)], fill=C['start'], stroke='#2E7D32',
                         sw=0.3, runs=lab, size=6, bold=True, textbox=lbl_below, valign='top')
        if k == 'end':
            return Shape(x, y, w, h, [('ell', w / 2, h / 2, w / 2, h / 2)], fill=C['end'], stroke='#000000',
                         sw=0.9, runs=lab, size=6, bold=True, textbox=lbl_below, valign='top')
        if k in ('timer', 'timer_start'):
            r = w / 2
            geo = [('ell', r, r, r, r), ('ell', r, r, r - 1, r - 1), ('ell', r, r, r - 2, r - 2),
                   ('poly', [(r, r - 2.6), (r, r), (r + 1.8, r + 0.9)], False)]
            fill = C['timer'] if k == 'timer' else '#C8E6C9'
            return Shape(x, y, w, h, geo, fill=fill, stroke='#000000', sw=0.3, runs=lab, size=6, bold=True,
                         textbox=lbl_below, valign='top')
        if k in ('msg', 'msg_start', 'msg_end'):
            r = w / 2
            ex, ey, ew, eh = r - 2.6, r - 1.8, 5.2, 3.6
            geo = [('ell', r, r, r, r)]
            if k == 'msg':
                geo.append(('ell', r, r, r - 1, r - 1))
            geo += [('poly', [(ex, ey), (ex + ew, ey), (ex + ew, ey + eh), (ex, ey + eh)], True),
                    ('poly', [(ex, ey), (r, ey + 2), (ex + ew, ey)], False)]
            fill = {'msg_start': '#C8E6C9', 'msg': '#DCE8FB', 'msg_end': '#FFCDD2'}[k]
            return Shape(x, y, w, h, geo, fill=fill, stroke='#000000', sw=0.9 if k == 'msg_end' else 0.3,
                         runs=lab, size=6, bold=True, textbox=lbl_below, valign='top')
        if k.startswith('gate'):
            geo = [('poly', [(w / 2, 0), (w, h / 2), (w / 2, h), (0, h / 2)], True)]
            if k == 'gate_xor':
                d = 2.4
                geo += [('poly', [(w / 2 - d, h / 2 - d), (w / 2 + d, h / 2 + d)], False),
                        ('poly', [(w / 2 + d, h / 2 - d), (w / 2 - d, h / 2 + d)], False)]
            else:
                d = 3
                geo += [('poly', [(w / 2 - d, h / 2), (w / 2 + d, h / 2)], False),
                        ('poly', [(w / 2, h / 2 - d), (w / 2, h / 2 + d)], False)]
            lp = n.get('lpos', 'top')
            tb, va, ha = {'top': ((-12, -10, w + 24, 9.5), 'bottom', 'center'),
                          'bottom': ((-12, h + 0.5, w + 24, 9.5), 'top', 'center'),
                          'tr': ((w / 2 + 1.5, -9, 30, 8.5), 'bottom', 'left')}[lp]
            return Shape(x, y, w, h, geo, fill=C['gate'], stroke='#000000', sw=0.35, runs=lab, size=6,
                         bold=True, textbox=tb, valign=va, halign=ha)
        if k == 'data':
            f = 2.5
            geo = [('poly', [(0, 0), (w - f, 0), (w, f), (w, h), (0, h)], True),
                   ('poly', [(w - f, 0), (w - f, f), (w, f)], False)]
            return Shape(x, y, w, h, geo, fill=C['data'], stroke='#000000', sw=0.3, runs=lab, size=5.5,
                         textbox=(-12, h + 0.6, w + 24, 8), valign='top')
        raise ValueError(k)

    def render(self):
        S = self._header() + self._pool()
        for e in self.edges:
            if e['assoc']:   # data association: straight dotted line, no arrow
                A, B = self.nodes[e['a']], self.nodes[e['b']]
                S.append(line([self.side(A, e['exit'] or 't'), self.side(B, e['enter'] or 'b')],
                              dash=3, arrow=False, sw=0.25, stroke=C['note']))
                continue
            pts = self._route(e)
            S.append(line(pts, dash=2 if e['msg'] else 0, sw=0.3))
            if e['label']:
                (x1, y1), (x2, y2) = pts[0], pts[1]
                if abs(y1 - y2) < 0.1 and x2 < x1:   # leaves to the left
                    S.append(text(x1 - 40.8, y1 - 4.2, 40, 4, e['label'], size=5.8, bold=True,
                                  halign='right', color=C['ink']))
                elif abs(y1 - y2) < 0.1:   # leaves to the right
                    S.append(text(x1 + 0.8, y1 - 4.2, 40, 4, e['label'], size=5.8, bold=True,
                                  halign='left', color=C['ink']))
                else:
                    S.append(text(x1 + 0.8, y1 + (0.5 if y2 > y1 else -4.6), 40, 4, e['label'],
                                  size=5.8, bold=True, halign='left', color=C['ink']))
        for n in self.nodes.values():
            S.append(self._node(n))
        S += self.extra
        return S
