#!/usr/bin/pyhton3

import requests
from bs4 import BeautifulSoup
import csv

def scrape_hacker_news():
    url = "https://news.ycombinator.com/"
    response = requests.get(url)

    if response.status_code != 200:
        print("Failed...")
        return

    soup = BeautifulSoup(response.text, 'html.parser')
    headlines = soup.select('.titleline')

    data = []

    for idx, item in enumerate(headlines, start=1):
        title = item.get_text()
        link = item.find('a')['href']
        print(f"{idx}. {title} ({link})")
        data.append([idx, title, link])

    with open("hacker_news_headlines.csv", "w", newline="", encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["No", "Title", "Link"])
        writer.writerows(data)

    print("\nSaved to hacker_news_headlines.csv")

if __name__ == "__main__":
    scrape_hacker_news()
