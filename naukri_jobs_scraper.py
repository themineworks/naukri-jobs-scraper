#!/usr/bin/env python3
"""India's largest job board structured as clean JSON. Python, Node.js and cURL clients for the Naukri Job Scraper on Apify, pay per result.

Command-line client for the themineworks/naukri-jobs actor on Apify: runs it, waits for it
to finish and saves every result as JSON and CSV. Flags map 1:1 to the actor's input.
Free Apify account and API token: https://console.apify.com/sign-up
Docs and pricing: https://themineworks.com/actors/naukri-jobs/
"""
import argparse, csv, json, os, sys
from apify_client import ApifyClient

ACTOR = "themineworks/naukri-jobs"


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--token", default=os.environ.get("APIFY_TOKEN"), help="Apify API token (or set APIFY_TOKEN)")
    ap.add_argument("--out", default="results", help="Output basename, writes .json and .csv")
    ap.add_argument("--search-keywords", help="Comma-separated. One or more job-search keywords")
    ap.add_argument("--location", help="City or region, for example 'Bangalore', 'Mumbai', 'Delhi NCR'")
    ap.add_argument("--job-type", help="Employment type to filter for, such as permanent, contract, or internship")
    ap.add_argument("--work-mode", help="Where the work happens: from the office, fully remote, or a hybrid mix")
    ap.add_argument("--posted-within-days", help="Only show jobs posted within the last N days")
    ap.add_argument("--max-jobs", type=int, help="Maximum number of jobs to scrape across all keywords")
    ap.add_argument("--include-job-description", action=argparse.BooleanOptionalAction, help="If true, include the full job description text")
    ap.add_argument("--monitor-mode", action=argparse.BooleanOptionalAction, help="Run on a schedule and deliver ONLY results not seen in a previous run")
    ap.add_argument("--experience-min-years", type=int, help="Minimum years of experience")
    ap.add_argument("--experience-max-years", type=int, help="Maximum years of experience")
    ap.add_argument("--salary-min-lakhs", type=int, help="Minimum annual CTC in INR Lakhs")
    a = ap.parse_args()
    if not a.token:
        sys.exit("Provide --token or set APIFY_TOKEN. Free token: https://console.apify.com/sign-up")

    run_input = {}
    if a.search_keywords: run_input["searchKeywords"] = [s.strip() for s in a.search_keywords.split(",") if s.strip()]
    if a.location is not None: run_input["location"] = a.location
    if a.job_type is not None: run_input["jobType"] = a.job_type
    if a.work_mode is not None: run_input["workMode"] = a.work_mode
    if a.posted_within_days is not None: run_input["postedWithinDays"] = a.posted_within_days
    if a.max_jobs is not None: run_input["maxJobs"] = a.max_jobs
    if a.include_job_description is not None: run_input["includeJobDescription"] = a.include_job_description
    if a.monitor_mode is not None: run_input["monitorMode"] = a.monitor_mode
    if a.experience_min_years is not None: run_input["experienceMinYears"] = a.experience_min_years
    if a.experience_max_years is not None: run_input["experienceMaxYears"] = a.experience_max_years
    if a.salary_min_lakhs is not None: run_input["salaryMinLakhs"] = a.salary_min_lakhs

    client = ApifyClient(a.token)
    print(f"Running {ACTOR} ...")
    run = client.actor(ACTOR).call(run_input=run_input)
    items = list(client.dataset(run["defaultDatasetId"]).iterate_items())

    with open(a.out + ".json", "w", encoding="utf-8") as f:
        json.dump(items, f, indent=2, ensure_ascii=False)
    keys = []
    for it in items:
        keys += [k for k in it if k not in keys]
    if items:
        with open(a.out + ".csv", "w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=keys, extrasaction="ignore")
            w.writeheader()
            for it in items:
                w.writerow({k: json.dumps(v, ensure_ascii=False) if isinstance(v, (list, dict)) else v for k, v in it.items()})
    print(f"Done: {len(items)} results saved to {a.out}.json and {a.out}.csv")


if __name__ == "__main__":
    main()
