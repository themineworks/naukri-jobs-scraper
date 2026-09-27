# Naukri Job Scraper: India Jobs, Salary & Skills Data

Scrape Naukri.com job listings: title, company, salary (normalised to lakhs per annum), experience required, skills, location, work mode, and direct application URL. India's #1 job board with 100,000+ live listings. Pay only per job returned.

**Run it on Apify:** [apify.com/themineworks/naukri-jobs](https://apify.com/themineworks/naukri-jobs)
**Docs, FAQ and pricing:** [themineworks.com/actors/naukri-jobs](https://themineworks.com/actors/naukri-jobs/)

**Price:** $1.40 per 1,000 jobs on Apify's free plan, down to $0.84 on higher plans, plus a $0.005 start fee per run. Failed and empty results are never charged.

## What it returns

* Job title, company, and salary in lakhs
* Experience range and required skills
* Location, work mode (WFH/hybrid/office)
* Direct application URL per listing
* Zero charge on empty searches

## Quick start

You need a free [Apify account](https://console.apify.com/sign-up) and its API token (Settings, API & Integrations).

### Python

```bash
pip install apify-client
```

```python
from apify_client import ApifyClient

client = ApifyClient("YOUR_APIFY_TOKEN")
run = client.actor("themineworks/naukri-jobs").call(run_input={
    "searchKeywords": [
        "python developer"
    ],
    "location": "Bangalore",
    "jobType": "permanent",
    "workMode": "hybrid"
})

for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(item)
```

### Node.js

```bash
npm install apify-client
```

```javascript
import { ApifyClient } from 'apify-client';

const client = new ApifyClient({ token: 'YOUR_APIFY_TOKEN' });
const run = await client.actor('themineworks/naukri-jobs').call({
    "searchKeywords": [
        "python developer"
    ],
    "location": "Bangalore",
    "jobType": "permanent",
    "workMode": "hybrid"
});
const { items } = await client.dataset(run.defaultDatasetId).listItems();
console.log(items);
```

### cURL

One request that runs the actor and returns the results in the response (for runs under 5 minutes):

```bash
curl -X POST "https://api.apify.com/v2/acts/themineworks~naukri-jobs/run-sync-get-dataset-items?token=YOUR_APIFY_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"searchKeywords": ["python developer"], "location": "Bangalore", "jobType": "permanent", "workMode": "hybrid"}'
```

### Command line

This repo includes ready-made clients that save results to JSON and CSV:

```bash
python3 naukri_jobs_scraper.py --token YOUR_APIFY_TOKEN --search-keywords "python developer" --location "Bangalore" --job-type "permanent" --work-mode "hybrid"
node naukri_jobs_scraper.mjs --token YOUR_APIFY_TOKEN --search-keywords "python developer" --location "Bangalore" --job-type "permanent" --work-mode "hybrid"
```

## Input

| Field | Type | Default | Description |
|---|---|---|---|
| `searchKeywords` (required) | array |  | One or more job-search keywords |
| `location` | string |  | City or region, for example 'Bangalore', 'Mumbai', 'Delhi NCR' |
| `jobType` | string |  | Employment type to filter for, such as permanent, contract, or internship |
| `workMode` | string |  | Where the work happens: from the office, fully remote, or a hybrid mix |
| `postedWithinDays` | string |  | Only show jobs posted within the last N days |
| `maxJobs` | integer | `5` | Maximum number of jobs to scrape across all keywords |
| `includeJobDescription` | boolean | `false` | If true, include the full job description text |
| `monitorMode` | boolean | `false` | Run on a schedule and deliver ONLY results not seen in a previous run |
| `experienceMinYears` | integer |  | Minimum years of experience |
| `experienceMaxYears` | integer |  | Maximum years of experience |
| `salaryMinLakhs` | integer |  | Minimum annual CTC in INR Lakhs |

## Output

One row per result, as JSON, CSV, Excel or through the API.

| Field | Type | Description |
|---|---|---|
| `job_id` | string | Naukri internal job ID |
| `title` | string | Job title |
| `company` | string | Company name |
| `location` | string | Job location(s) from Naukri placeholder |
| `experience_min_years` | number | Minimum years of experience required |
| `experience_max_years` | number | Maximum years of experience required |
| `experience_text` | string | Raw experience text (for example '5-10 Yrs') |
| `salary_text` | string | Raw salary string from Naukri |
| `salary_min_lakhs` | number | Minimum salary in lakhs per annum |
| `salary_max_lakhs` | number | Maximum salary in lakhs per annum |
| `work_mode` | string | Work mode (remote, hybrid, work-from-office) |
| `job_type` | string | Job type (permanent, contract, internship, etc.) |
| `skills` | array | Required skills list |
| `description` | string | Job description text (truncated to 500 chars unless includeJobDescription=true) |
| `apply_url` | string | URL to the Naukri job detail / apply page |
| `posted_date_text` | string | Raw posted date text from Naukri |
| `posted_days_ago` | number | Approximate number of days since the job was posted |
| `scraped_at` | string | ISO timestamp when this record was scraped |

## Use it from an AI agent

The actor works as a tool in Claude, Cursor or any MCP client through Apify's MCP server:

```
https://mcp.apify.com/?tools=themineworks/naukri-jobs
```

## FAQ

### Does Naukri have an official API?

No. Naukri.com does not offer a public API for job listings. This scraper accesses live search results and returns structured data per listing.

### What fields does each job listing include?

Job title, company name, salary range normalised to lakhs per annum, years of experience required, required skills list, location, work mode (work from home, hybrid, or office), and the direct Naukri job URL.

### Can I filter by skills or experience level?

Yes. Search queries accept keywords, skills, location, and experience range. Use the same search terms you would use on Naukri.com. They translate directly to the scraper's input.

### What is the typical use case?

Hiring intelligence and talent market research: track which skills are in demand, benchmark salary ranges by role and city, monitor competitor job postings, or build job aggregation tools for the Indian market.

### How current is the data?

Each run fetches live results from Naukri.com at the time of execution. Job listings are added and removed continuously, so run on a schedule to capture changes over time.

### How much does the Naukri Job Scraper cost?

$1.40 per 1,000 jobs on Apify's free plan, down to $0.84 on higher plans, plus a $0.005 start fee per run. Failed and empty results are never charged. You can cap what a single run may spend with the maximum cost setting on Apify.

### Can I export the results to CSV or Excel?

Yes. Every run saves to an Apify dataset you can download as JSON, CSV, Excel or XML, or read through the API. The Python and Node clients in this repo also write the results to local files.

### Can I run it on a schedule?

Yes. Save your input as a task on Apify and attach a schedule, or call the API from your own cron job. Scheduled runs are billed the same way as manual ones.

## Related scrapers

* [Foundit Jobs Scraper](https://themineworks.com/actors/foundit-jobs-scraper/): Foundit.in (Monster India): 20 fields, monitor mode
* [Hirist Jobs Scraper](https://themineworks.com/actors/hirist-jobs-scraper/): India IT jobs across 147 locations, 19 fields
* [Shine.com Jobs Scraper](https://themineworks.com/actors/shine-jobs-scraper/): Times Group India job board, 22 fields, monitor mode

Part of [The Mine Works](https://themineworks.com/): 151 pay-per-result scrapers with no login and no browser setup on your side.

## License

MIT © The Mine Works
