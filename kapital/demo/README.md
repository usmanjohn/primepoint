# Risk Dashboard — demo on synthetic data

The portfolio part of my internal risk dashboard, running on **invented data**
so it can be shown outside the bank. The pages, views, charts and styles are my
own bank code, copied unchanged except for the list below.

## Run it

    pip install -r requirements.txt
    python -c "import plotly.offline as o; open('static/js/plotly.min.js','w').write(o.get_plotlyjs())"
    python make_fake_svod.py datasets/portfel/svod --months 12   # fake data
    python manage.py runserver                                   # http://127.0.0.1:8000

No database, no Oracle, no accounts: every visitor is a read-only guest.

## Where the data come from

`make_fake_svod.py` writes one `svod_<date>.parquet` per month with the same
columns the bank's processing step (`process_portfel_best`) produces. Every
number is generated: the scale (~2.5 trillion), the department split, the NPL
shares, the branch mix. Branch names are plain Tashkent districts and regional
cities, not the bank's branch names.

## What was changed from the bank version (and nothing else)

| File | Change |
|---|---|
| `templates/base.html` | logo → "Risk Dashboard DEMO" text, page title, yellow "synthetic data" banner |
| `portfel/views.py` | only `portfel_home`, `portfel_result`, `download_portfel_summary`; no Oracle step |
| `portfel/urls.py` | `get` / `process` / `compare` removed (they need the bank database) |
| `portfel/functions.py` | `region_t` (Tashkent branches) → neutral district names |
| `portfel/templates/portfel/result_total.html` | the tooltip listing Tashkent branches → same neutral names |
| `functions/common_functions.py` | Oracle connection removed |
| `general/views.py` | `home` + an "internal only" page for sections that need the bank database |
| new | `demo_site/` (settings, guest user), `general/formatters.py`, `make_fake_svod.py` |

## On Powerty

The demo is served **frozen** at `powerty.uz/about/me/demo/`: `freeze.py` renders
every page for every month into plain HTML (links made relative, the date form
turned into month buttons), and Powerty serves the files (`prime.views.demo_dashboard`).
To refresh it:

    python make_fake_svod.py datasets/portfel/svod --months 6
    python freeze.py ../../prime/demo_dashboard \
        --static-dir ../../static/demo_dashboard --static-url /static/demo_dashboard/

then run `python manage.py test prime.tests.DemoDashboardTests` from the repo root and commit
`prime/demo_dashboard/` + `static/demo_dashboard/`.
