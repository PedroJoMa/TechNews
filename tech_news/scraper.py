import requests
import time
from parsel import Selector


# Requisito 1
def fetch(url):
    try:
        headers = {"User-Agent": "Fake user-agent"}
        response = requests.get(url, headers=headers, timeout=3)
        time.sleep(1)
        if (response.status_code == 200):
            return response.text
        else:
            return None
    except requests.ReadTimeout:
        return None


# Requisito 2
def scrape_updates(html_content):
    selector = Selector(text=html_content)
    urls = selector.css("h2.entry-title a::attr(href)").getall()
    return urls


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(text=html_content)
    next_page_link = selector.css(
        "div.nav-links a.next.page-numbers::attr(href)"
    ).get()
    return next_page_link


# Requisito 4
def scrape_news(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
