import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime
import argparse
import time

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Educational Scraper)"
}

def date_in_range(date_str, start, end):
    review_date = datetime.strptime(date_str, "%Y-%m-%d")
    return start <= review_date <= end


# -------------------- G2 SCRAPER --------------------
def scrape_g2(company, start, end):
    reviews = []
    page = 1

    while True:
        url = f"https://www.g2.com/products/{company}/reviews?page={page}"
        res = requests.get(url, headers=HEADERS)

        if res.status_code != 200:
            break

        soup = BeautifulSoup(res.text, "html.parser")
        cards = soup.select("div.paper")

        if not cards:
            break

        for card in cards:
            try:
                title = card.select_one("h3").text.strip()
                body = card.select_one("div[itemprop='reviewBody']").text.strip()
                date = card.select_one("time")["datetime"][:10]
                rating = card.select_one("meta[itemprop='ratingValue']")["content"]
                reviewer = card.select_one("span[itemprop='author']").text.strip()

                if date_in_range(date, start, end):
                    reviews.append({
                        "title": title,
                        "review": body,
                        "date": date,
                        "reviewer": reviewer,
                        "rating": rating,
                        "source": "G2"
                    })
            except:
                continue

        page += 1
        time.sleep(1)

    return reviews


# -------------------- CAPTERRA SCRAPER --------------------
def scrape_capterra(company, start, end):
    reviews = []
    page = 1

    while True:
        url = f"https://www.capterra.com/p/{company}/reviews/?page={page}"
        res = requests.get(url, headers=HEADERS)

        if res.status_code != 200:
            break

        soup = BeautifulSoup(res.text, "html.parser")
        cards = soup.select("div.review")

        if not cards:
            break

        for card in cards:
            try:
                title = card.select_one("h3").text.strip()
                body = card.select_one("p").text.strip()
                date = card.select_one("time")["datetime"][:10]
                rating = card.select_one("span.star-rating")["aria-label"]
                reviewer = card.select_one("span.reviewer").text.strip()

                if date_in_range(date, start, end):
                    reviews.append({
                        "title": title,
                        "review": body,
                        "date": date,
                        "reviewer": reviewer,
                        "rating": rating,
                        "source": "Capterra"
                    })
            except:
                continue

        page += 1
        time.sleep(1)

    return reviews


# -------------------- BONUS: TRUST RADIUS SCRAPER --------------------
def scrape_trustradius(company, start, end):
    reviews = []
    page = 1

    while True:
        url = f"https://www.trustradius.com/products/{company}/reviews?page={page}"
        res = requests.get(url, headers=HEADERS)

        if res.status_code != 200:
            break

        soup = BeautifulSoup(res.text, "html.parser")
        cards = soup.select("div.review")

        if not cards:
            break

        for card in cards:
            try:
                title = card.select_one("h3").text.strip()
                body = card.select_one("p").text.strip()
                date = card.select_one("time")["datetime"][:10]
                rating = card.select_one("span.rating").text.strip()
                reviewer = card.select_one("span.author").text.strip()

                if date_in_range(date, start, end):
                    reviews.append({
                        "title": title,
                        "review": body,
                        "date": date,
                        "reviewer": reviewer,
                        "rating": rating,
                        "source": "TrustRadius"
                    })
            except:
                continue

        page += 1
        time.sleep(1)

    return reviews


# -------------------- MAIN FUNCTION --------------------
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--company", required=True)
    parser.add_argument("--start", required=True)
    parser.add_argument("--end", required=True)
    parser.add_argument("--source", required=True)

    args = parser.parse_args()

    start = datetime.strptime(args.start, "%Y-%m-%d")
    end = datetime.strptime(args.end, "%Y-%m-%d")

    if start > end:
        raise ValueError("Start date must be before end date")

    if args.source.lower() == "g2":
        data = scrape_g2(args.company, start, end)
    elif args.source.lower() == "capterra":
        data = scrape_capterra(args.company, start, end)
    elif args.source.lower() == "trustradius":
        data = scrape_trustradius(args.company, start, end)
    else:
        raise ValueError("Invalid source")

    with open("reviews.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

    print(f"Saved {len(data)} reviews to reviews.json")


if __name__ == "__main__":
    main()
