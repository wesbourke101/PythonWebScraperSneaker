import requests
from bs4 import BeautifulSoup
from scraper_for_nike_talk import scrape_nike_talk_page

#get number of pages programatically 
total_pages = 40

#page number
page_number = 1

# URL of the NikeTalk forum
base_url = 'https://niketalk.com/forums/jordan-brand.7348/'

if page_number == 1:
    scrape_nike_talk_page(base_url)
    page_number += 1
for page in range(1, total_pages + 1):
    page_url = f"{base_url}page-{page_number}"
    print(f"Scraping page {page_number}: {page_url}")
    scrape_nike_talk_page(page_url)
    page_number += 1