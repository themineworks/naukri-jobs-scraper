#!/usr/bin/env python3
"""Search Naukri.com job listings with salary, company and skills — no login.
CLI for the themineworks/naukri-jobs Apify actor: runs it, waits, saves JSON + CSV.
Free Apify account + API token: https://console.apify.com/sign-up
"""
import argparse, csv, json, os, sys
from apify_client import ApifyClient

ACTOR = "themineworks/naukri-jobs"

def main():
    ap = argparse.ArgumentParser(description="search Naukri.com job listings with salary, company and skills — no login")
    ap.add_argument("--token", default=os.environ.get("APIFY_TOKEN"),
                    help="Apify API token (or set APIFY_TOKEN env var)")
    ap.add_argument("--out", default="results", help="Output basename (.json and .csv)")
    ap.add_argument("--search-keywords", help="Comma-separated. One or more job-search keywords e.g. python developer")
    ap.add_argument("--max-jobs", type=int, default=5, help="Maximum number of jobs to scrape across all keywords")
    ap.add_argument("--include-job-description", action="store_true", help="If true, include the full job description text")
    ap.add_argument("--location", help="City or region, e.g. 'Bangalore', 'Mumbai', 'Delhi NCR'")
    ap.add_argument("--experience-min-years", type=int, help="Minimum years of experience")
    ap.add_argument("--experience-max-years", type=int, help="Maximum years of experience")
    ap.add_argument("--salary-min-lakhs", type=int, help="Minimum annual CTC in INR Lakhs")
    a = ap.parse_args()
    if not a.token:
        sys.exit("Provide --token or set APIFY_TOKEN — free token at https://console.apify.com/sign-up")

    run_input = {}
    if a.search_keywords is not None: run_input["searchKeywords"] = [s.strip() for s in a.search_keywords.split(",") if s.strip()]
    if a.max_jobs is not None: run_input["maxJobs"] = a.max_jobs
    if a.include_job_description: run_input["includeJobDescription"] = True
    if a.location is not None: run_input["location"] = a.location
    if a.experience_min_years is not None: run_input["experienceMinYears"] = a.experience_min_years
    if a.experience_max_years is not None: run_input["experienceMaxYears"] = a.experience_max_years
    if a.salary_min_lakhs is not None: run_input["salaryMinLakhs"] = a.salary_min_lakhs

    client = ApifyClient(a.token)
    print(f"Running {ACTOR} ...")
    run = client.actor(ACTOR).call(run_input=run_input)
    items = list(client.dataset(run["defaultDatasetId"]).iterate_items())

    with open(a.out + ".json", "w", encoding="utf-8") as f:
        json.dump(items, f, indent=2, ensure_ascii=False)
    if items:
        keys = []
        for it in items:
            for k in it:
                if k not in keys: keys.append(k)
        with open(a.out + ".csv", "w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=keys, extrasaction="ignore")
            w.writeheader()
            for it in items:
                w.writerow({k: ("" if v is None else v) for k, v in it.items()})
    print(f"Done: {len(items)} results -> {a.out}.json / {a.out}.csv")

if __name__ == "__main__":
    main()
