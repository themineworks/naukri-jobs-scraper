# Naukri Jobs Scraper — Salary, Company, Skills, No Login

Python client for **[Naukri Jobs Scraper — Salary, Company, Skills, No Login](https://apify.com/themineworks/naukri-jobs)** — search Naukri.com job listings with salary, company and skills — no login.

> ⚡ No login, no cookies, no ban risk · runs in the cloud on [Apify](https://apify.com/themineworks/naukri-jobs)
>
> 💸 From **$1.4 per 1,000 results** (volume discounts on paid Apify plans). You are only charged for delivered results — empty searches and failed pages are never billed.

## Quick start

```bash
pip install apify-client
python3 naukri_jobs_scraper.py --token YOUR_APIFY_TOKEN --search-keywords "python developer"
```

Get a free API token: [console.apify.com/sign-up](https://console.apify.com/sign-up) — then find it under **Settings → API & Integrations**.

## Options

| Flag | Type | Description |
|---|---|---|
| `--token` | string | Apify API token (or `APIFY_TOKEN` env var) |
| `--out` | string | Output basename — writes `results.json` + `results.csv` |
| `--search-keywords` | array | One or more job-search keywords. Each keyword is searched separately and results are merge |
| `--max-jobs` | integer | Maximum number of jobs to scrape across all keywords. Hard cap 1000. |
| `--include-job-description` | boolean | If true, include the full job description text. If false, descriptions are truncated to 50 |
| `--location` | string | City or region, e.g. 'Bangalore', 'Mumbai', 'Delhi NCR'. Leave blank for all India. |
| `--experience-min-years` | integer | Minimum years of experience. 0 = fresher. |
| `--experience-max-years` | integer | Maximum years of experience. |
| `--salary-min-lakhs` | integer | Minimum annual CTC in INR Lakhs. Naukri supports 3, 6, 10, 15, 25, 50, 75, 100. |

Flags map 1:1 to the actor's input schema — full reference and a live output sample on the [Store listing](https://apify.com/themineworks/naukri-jobs).

## Output

One row per result, saved as both JSON and CSV with every field the actor returns. Preview the exact fields on the [listing's output tab](https://apify.com/themineworks/naukri-jobs).

## Why this actor

- **HTTP-native** — fast, stable, no headless-browser overhead
- **No account risk** — never asks for your login or cookies
- **Fair billing** — pay per delivered result only

MIT © [The Mine Works](https://apify.com/themineworks) — part of a 69-scraper suite trusted by 450+ developers.
