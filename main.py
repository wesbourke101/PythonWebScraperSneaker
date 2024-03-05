import requests
from bs4 import BeautifulSoup
from scraper_for_nike_talk import scrape_nike_talk_page

# Get the number of pages programmatically
total_pages = 40

# Initialize page number
page_number = 1

# URL of the NikeTalk forum
base_url = 'https://niketalk.com/forums/jordan-brand.7348/'

# Dictionary to store page views and the topic name
order_list = []

# Scrape the first page
scrape_nike_talk_page(base_url, order_list)
page_number += 1

# Iterate over remaining pages
for page in range(1, total_pages + 1):
    page_url = f"{base_url}page-{page_number}"
    print(f"Scraping page {page_number}: {page_url}")
    scrape_nike_talk_page(page_url, order_list)
    page_number += 1

# Sort the dictionary by keys in descending order
sorted_order_list = sorted(order_list, key=lambda x: list(x.keys())[0], reverse=True)


# Print the ordered list
for x in sorted_order_list:
    print(x)