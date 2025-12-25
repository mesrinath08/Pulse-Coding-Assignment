# Pulse-Coding-Assignment
Pulse Coding Assignment – Product Review Scraper
Project Overview

This project implements a Python-based script that scrapes product reviews from popular SaaS review platforms. The script accepts a company name, a start date, an end date, and a review source as input, and outputs the collected reviews in a structured JSON format. The solution is designed for educational purposes and demonstrates web scraping, data parsing, pagination handling, and error management.

Supported Review Sources

G2

Capterra

TrustRadius (Bonus SaaS review source)

Input Parameters

company: Name of the company/product whose reviews are to be scraped

start: Start date in YYYY-MM-DD format

end: End date in YYYY-MM-DD format

source: Review source (g2, capterra, or trustradius)

Output

The script generates a file named reviews.json containing an array of review objects.
Each review includes:

Title

Review text

Date of posting

Reviewer name

Rating

Source

Project Structure
scrape_reviews.py
reviews.json
README.md

Installation

Ensure Python 3 is installed on your system.
Install the required dependencies using:

pip install requests beautifulsoup4

How to Run

Run the script from the command line using the following format:

python scrape_reviews.py --company <company_name> --start <start_date> --end <end_date> --source <source_name>

Example
python scrape_reviews.py --company slack --start 2023-01-01 --end 2023-12-31 --source g2

Features

Scrapes reviews based on company name and date range

Handles pagination automatically

Supports multiple review platforms

Outputs clean and structured JSON data

Includes basic error handling for invalid inputs

Bonus Source

TrustRadius has been integrated as an additional SaaS-focused review platform with the same functionality as G2 and Capterra.

Disclaimer

This project is created strictly for educational purposes. Web scraping should be performed responsibly and in accordance with the terms and conditions of the respective websites.
