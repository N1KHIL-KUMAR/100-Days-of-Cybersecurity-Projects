#!/usr/bin/python3

import requests
from urllib.parse import urljoin

def fetch_robots_txt(base_url):
    if not base_url.startswith('http'): #check first in url 
        base_url = 'http://' + base_url

    robots_url = urljoin(base_url, '/robots.txt')

    try:
        response = requests.get(robots_url, timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"[ERROR] Unable to fetch robots.txt: {e}")
        return None

    return response.text

def parse_robots_txt(content):
    sitemap_urls = []
    rules = []
    
    for line in content.splitlines():
        line = line.strip()
        if not line or line.startswith('#'):
            continue

        if line.lower().startswith('sitemap:'):
            sitemap_urls.append(line.split(':', 1)[1].strip())

        elif any(line.lower().startswith(k) for k in ['user-agent', 'disallow', 'allow', 'crawl-delay']):
            key, value = line.split(':', 1)
            rules.append((key.strip(), value.strip()))

    return rules, sitemap_urls

def display_results(rules, sitemaps):
    print("\n Robots.txt Rules:")
    for rule in rules:
        print(f"{rule[0]}: {rule[1]}")
    
    if sitemaps:
        print("\n Sitemap URLs:")
        for sitemap in sitemaps:
            print(sitemap)
    else:
        print("\n No sitemap URLs found.")

if __name__ == "__main__":
    website = input("[+]Enter website URL (e.g., example.com): ").strip()
    content = fetch_robots_txt(website)
    if content:
        rules, sitemaps = parse_robots_txt(content)
        display_results(rules, sitemaps)
