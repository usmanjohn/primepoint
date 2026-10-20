# -*- coding: utf-8 -*-
"""Regenerate tutorial/management/commands/_tutorials_code_law_pages.py from kapital/laws/*.html.

    python3 kapital/build_code_playlist.py

Lessons go into the admin-only "Kapital" playlist, numbered in the order to install them:
1 = views.py + urls.py, 2 = the laws home page, 3+ = one law page each.
To add a page: put the .html in kapital/laws/, append a row to PAGES (it gets the next number),
run this script, then import with --republish.
"""
import html
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
LAWS = ROOT / 'kapital' / 'laws'
OUT = ROOT / 'tutorial' / 'management' / 'commands' / '_tutorials_code_law_pages.py'

# (file stem, old title — kept only so the importer renames the lesson in place; name; summary; view; url path; url name)
PAGES = [
    ('law_capital_3697', 'Law page: Capital adequacy (CBU Regulation 3697)', 'Capital adequacy (CBU 3697)',
     'Django template: Basel III capital ratios, buffers, leverage and a live ratio calculator. Russian UI.',
     'law_capital', 'laws/capital/', 'laws-capital-3697'),
    ('law_liquidity_2709', 'Law page: Liquidity — LCR, NSFR (CBU Regulation 2709)', 'Liquidity — LCR, NSFR (CBU 2709)',
     'Django template: LCR, NSFR, instant liquidity, HQLA levels and an LCR calculator with level caps. Russian UI.',
     'law_liquidity', 'laws/liquidity/', 'laws-liquidity-2709'),
    ('law_large_exposure_3283', 'Law page: Large exposures (CBU Regulation 3283)', 'Large exposures (CBU 3283)',
     'Django template: single-borrower, group and related-party limits with an editable portfolio checker. Russian UI.',
     'law_large_exposure', 'laws/large-exposure/', 'laws-large-exposure-3283'),
    ('law_macroprudential_3618', 'Law page: Macroprudential limits — DSTI, DTI, LTV (CBU Regulation 3618)', 'Macroprudential limits — DSTI, DTI, LTV (CBU 3618)',
     'Django template: debt-burden, debt-to-income, LTV and concentration limits with a loan-application calculator. Russian UI.',
     'law_macroprudential', 'laws/macroprudential/', 'laws-macro-3618'),
    ('law_asset_quality_3937', 'Law page: Asset classification and provisions (CBU Regulation 3937)', 'Asset classification and provisions (CBU 3937)',
     'Django template: five asset classes, IFRS 9 link, collateral haircuts and a reserve calculator. Russian UI.',
     'law_asset_quality', 'laws/asset-quality/', 'laws-asset-quality-3937'),
    ('law_reserves_3002', 'Law page: Reserve requirements (CBU Regulation 3002)', 'Reserve requirements (CBU 3002)',
     'Django template: required reserves base, 4% / 7% norms, averaging on the correspondent account and a reserve calculator. Russian UI.',
     'law_reserves', 'laws/reserves/', 'laws-reserves-3002'),
    ('law_deposit_guarantee_1031', 'Law page: Deposit guarantee (Law ZRU-1031)', 'Deposit guarantee (Law ZRU-1031)',
     'Django template: 200 mln sum guarantee, what is covered, payout deadlines, bank contributions and a compensation calculator. Russian UI.',
     'law_deposit_guarantee', 'laws/deposit-guarantee/', 'laws-deposit-guarantee-1031'),
    ('law_risk_management_3427', 'Law page: Risk management system (CBU Regulation 3427)', 'Risk management system (CBU 3427)',
     'Django template: three lines of defence, risk appetite, CRO veto, reporting deadlines, problem assets and a risk-appetite traffic light. Russian UI.',
     'law_risk_management', 'laws/risk-management/', 'laws-risk-management-3427'),
    ('law_fx_position_3301', 'Law page: Open currency position (CBU Rules 3301)', 'Open currency position (CBU 3301)',
     'Django template: long/short FX positions, the four limit types, end-of-day rule and a multi-currency position calculator. Russian UI.',
     'law_fx_position', 'laws/fx-position/', 'laws-fx-position-3301'),
    ('law_irrbb_3427', 'Law page: Interest rate risk in the banking book (CBU Regulation 3427)', 'Interest rate risk in the banking book (CBU 3427)',
     'Django template: repricing gap, ΔEVE and ΔNII under the six rate scenarios, with a gap calculator. Russian UI.',
     'law_irrbb', 'laws/irrbb/', 'laws-irrbb-3427'),
    ('law_chart_of_accounts_3336', 'Law page: Chart of accounts (CBU, reg. 3336)', 'Chart of accounts (CBU, reg. 3336)',
     'Django template: 5- and 20-digit account numbers, classes, loan/deposit/off-balance families, loan entries, an account decoder and search over all ~1,200 accounts. Russian UI.',
     'law_chart_of_accounts', 'laws/chart-of-accounts/', 'laws-chart-of-accounts-3336'),
]

HEADER = '''# -*- coding: utf-8 -*-
"""Kapital playlist (admin only) — Django law-explainer templates (Russian UI) for a bank dashboard.

GENERATED from kapital/laws/*.html by kapital/build_code_playlist.py — edit the HTML files, then regenerate; do not edit by hand.
Lessons are numbered in install order: 1 views/urls, 2 home page, 3+ law pages.
Each lesson shows one template as a copyable code block. Facts checked against lex.uz and cbu.uz on 2026-10-15.

Import:
    python manage.py import_tutorials tutorial/management/commands/_tutorials_code_law_pages.py --author=prime
"""

PLAYLIST = {'title': 'Kapital', 'category': 'programming', 'staff_only': True,
            'description': 'Bank law-explainer pages, numbered in install order. Admin only.'}

TUTORIALS = []
'''


def code(src):
    return '<pre><code class="language-html">' + html.escape(src, quote=False) + '</code></pre>\n'


def lesson(order, name, old, summary, content):
    return 'TUTORIALS.append(' + repr({'title': f'{order}. {name}', 'renamed_from': [old],
                                       'category': 'programming', 'order': order,
                                       'summary': summary, 'content': content}) + ')\n'


def main():
    n = len(PAGES)
    out = [HEADER]

    views = '# views.py\nfrom django.shortcuts import render\n\n'
    views += '\n'.join(f'def {view}(request):\n    return render(request, "laws/{stem}.html")\n'
                       for stem, _, _, _, view, _, _ in PAGES)
    views += '\n\n# urls.py\nfrom django.urls import path\nfrom . import views\n\nurlpatterns += [\n'
    views += ''.join(f'    path("{url}", views.{view}, name="{name}"),\n' for _, _, _, _, view, url, name in PAGES)
    views += ']\n\n'
    out.append('\n' + lesson(1, 'Setup: views.py and urls.py', 'Law pages: views and urls',
                             f'Do this first: function-based views and URL names for the laws home page and all {n} law pages.',
                             f"<p>Step 1 of {n + 2}. Add these views and URLs first — every template links with "
                             f"<code>{{% url %}}</code>, and a missing URL name breaks the page. "
                             f"The home page also needs <code>laws-home</code> (your existing view).</p>\n"
                             '<h3>views.py · urls.py</h3>\n' + code(views)))

    home = (LAWS / 'home.html').read_text()
    out.append('\n' + lesson(2, 'Laws home page (all cards)', 'Law pages: home page with all cards',
                             f'Step 2: the laws home page with a card for each of the {n} law pages. Russian UI.',
                             f'<p>Step 2 of {n + 2}. Save as <code>templates/laws/home.html</code>. '
                             'Card links use the URL names from step 1.</p>\n<h3>home.html</h3>\n' + code(home)))

    for k, (stem, old, name, summary, *_rest) in enumerate(PAGES, start=3):
        src = (LAWS / f'{stem}.html').read_text()
        intro = (f'<p>Step {k} of {n + 2}. Django template <code>{stem}.html</code>. Extends <code>base.html</code>, '
                 f'all CSS is scoped under <code>.lw</code>, Bootstrap 5 + Font Awesome 6 from the base. Save it as '
                 f'<code>templates/laws/{stem}.html</code>.</p>\n<h3>{stem}.html</h3>\n')
        out.append('\n' + lesson(k, name, old, summary, intro + code(src)))

    OUT.write_text(''.join(out))
    print('wrote', OUT.relative_to(ROOT), f'({n + 2} numbered lessons)')


if __name__ == '__main__':
    main()
