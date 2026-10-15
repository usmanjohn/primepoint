# -*- coding: utf-8 -*-
"""Regenerate tutorial/management/commands/_tutorials_code_law_pages.py from kapital/laws/*.html.

    python3 kapital/build_code_playlist.py

Each law page becomes one lesson in the "Code" playlist showing the template as a copyable block.
To add a page: put the .html in kapital/laws/, add a row to PAGES, run this script, then import.
"""
import html
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
LAWS = ROOT / 'kapital' / 'laws'
OUT = ROOT / 'tutorial' / 'management' / 'commands' / '_tutorials_code_law_pages.py'

# (file stem, lesson title — the importer's match key, never reword it; order; summary; view name; url path; url name)
PAGES = [
    ('law_capital_3697', 'Law page: Capital adequacy (CBU Regulation 3697)', 1,
     'Django template: Basel III capital ratios, buffers, leverage and a live ratio calculator. Russian UI.',
     'law_capital', 'laws/capital/', 'laws-capital-3697'),
    ('law_liquidity_2709', 'Law page: Liquidity — LCR, NSFR (CBU Regulation 2709)', 2,
     'Django template: LCR, NSFR, instant liquidity, HQLA levels and an LCR calculator with level caps. Russian UI.',
     'law_liquidity', 'laws/liquidity/', 'laws-liquidity-2709'),
    ('law_large_exposure_3283', 'Law page: Large exposures (CBU Regulation 3283)', 3,
     'Django template: single-borrower, group and related-party limits with an editable portfolio checker. Russian UI.',
     'law_large_exposure', 'laws/large-exposure/', 'laws-large-exposure-3283'),
    ('law_macroprudential_3618', 'Law page: Macroprudential limits — DSTI, DTI, LTV (CBU Regulation 3618)', 4,
     'Django template: debt-burden, debt-to-income, LTV and concentration limits with a loan-application calculator. Russian UI.',
     'law_macroprudential', 'laws/macroprudential/', 'laws-macro-3618'),
    ('law_asset_quality_3937', 'Law page: Asset classification and provisions (CBU Regulation 3937)', 5,
     'Django template: five asset classes, IFRS 9 link, collateral haircuts and a reserve calculator. Russian UI.',
     'law_asset_quality', 'laws/asset-quality/', 'laws-asset-quality-3937'),
    ('law_reserves_3002', 'Law page: Reserve requirements (CBU Regulation 3002)', 8,
     'Django template: required reserves base, 4% / 7% norms, averaging on the correspondent account and a reserve calculator. Russian UI.',
     'law_reserves', 'laws/reserves/', 'laws-reserves-3002'),
    ('law_deposit_guarantee_1031', 'Law page: Deposit guarantee (Law ZRU-1031)', 9,
     'Django template: 200 mln sum guarantee, what is covered, payout deadlines, bank contributions and a compensation calculator. Russian UI.',
     'law_deposit_guarantee', 'laws/deposit-guarantee/', 'laws-deposit-guarantee-1031'),
    ('law_risk_management_3427', 'Law page: Risk management system (CBU Regulation 3427)', 10,
     'Django template: three lines of defence, risk appetite, CRO veto, reporting deadlines, problem assets and a risk-appetite traffic light. Russian UI.',
     'law_risk_management', 'laws/risk-management/', 'laws-risk-management-3427'),
    ('law_fx_position_3301', 'Law page: Open currency position (CBU Rules 3301)', 11,
     'Django template: long/short FX positions, the four limit types, end-of-day rule and a multi-currency position calculator. Russian UI.',
     'law_fx_position', 'laws/fx-position/', 'laws-fx-position-3301'),
    ('law_irrbb_3427', 'Law page: Interest rate risk in the banking book (CBU Regulation 3427)', 12,
     'Django template: repricing gap, ΔEVE and ΔNII under the six rate scenarios, with a gap calculator. Russian UI.',
     'law_irrbb', 'laws/irrbb/', 'laws-irrbb-3427'),
]

HEADER = '''# -*- coding: utf-8 -*-
"""Code playlist — Django law-explainer templates (Russian UI) for a bank dashboard.

GENERATED from kapital/laws/*.html by kapital/build_code_playlist.py — edit the HTML files, then regenerate; do not edit by hand.
Each lesson shows one template as a copyable code block. Facts checked against lex.uz and cbu.uz on 2026-10-15.

Import:
    python manage.py import_tutorials tutorial/management/commands/_tutorials_code_law_pages.py --author=prime
"""

PLAYLIST = {'title': 'Code', 'category': 'programming', 'description': 'Ready-to-paste code: Django templates and snippets.'}

TUTORIALS = []
'''


def code(src):
    return '<pre><code class="language-html">' + html.escape(src, quote=False) + '</code></pre>\n'


def lesson(title, order, summary, content):
    return 'TUTORIALS.append(' + repr({'title': title, 'category': 'programming', 'order': order,
                                       'summary': summary, 'content': content}) + ')\n'


def main():
    n = len(PAGES)
    out = [HEADER]
    for stem, title, order, summary, *_ in PAGES:
        src = (LAWS / f'{stem}.html').read_text()
        intro = (f'<p>Django template <code>{stem}.html</code>. Extends <code>base.html</code>, all CSS is scoped under '
                 f'<code>.lw</code>, Bootstrap 5 + Font Awesome 6 from the base. Save it as '
                 f'<code>templates/laws/{stem}.html</code>.</p>\n<h3>{stem}.html</h3>\n')
        out.append('\n' + lesson(title, order, summary, intro + code(src)))

    views = '# views.py\nfrom django.shortcuts import render\n\n'
    views += '\n'.join(f'def {view}(request):\n    return render(request, "laws/{stem}.html")\n'
                       for stem, _, _, _, view, _, _ in PAGES)
    views += '\n\n# urls.py\nfrom django.urls import path\nfrom . import views\n\nurlpatterns += [\n'
    views += ''.join(f'    path("{url}", views.{view}, name="{name}"),\n' for _, _, _, _, view, url, name in PAGES)
    views += ']\n\n'
    out.append('\n' + lesson('Law pages: views and urls', 6,
                             f'Function-based views and URL names for the {n} law-explainer templates and their home page.',
                             f"<p>Wiring for the {n} law pages. The templates link back with <code>{{% url 'laws-home' %}}</code>.</p>\n"
                             '<h3>views.py · urls.py · card</h3>\n' + code(views)))

    home = (LAWS / 'home.html').read_text()
    out.append('\n' + lesson('Law pages: home page with all cards', 7,
                             f'Django template: the laws home page linking the {n} law-explainer pages. Russian UI.',
                             '<p>Django template <code>home.html</code> for the laws section. Links use the URL names from the '
                             'views and urls lesson.</p>\n<h3>home.html</h3>\n' + code(home)))
    OUT.write_text(''.join(out))
    print('wrote', OUT.relative_to(ROOT), f'({n} pages + views + home)')


if __name__ == '__main__':
    main()
