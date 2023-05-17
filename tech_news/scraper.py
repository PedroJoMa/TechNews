import requests
import time
from parsel import Selector
from tech_news.database import create_news


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
    selector = Selector(text=html_content)
    notice_data = {}
    notice_data["url"] = (
        selector.css("link[rel='canonical']::attr(href)").get()
    )
    notice_data["title"] = (
        selector.css("h1.entry-title::text").get().strip()
    )
    notice_data["timestamp"] = (
        selector.css("li.meta-date::text").get()
    )
    notice_data["writer"] = (
        selector.css("span.author a::text").get()
    )
    notice_data["reading_time"] = int(
        selector.css("li.meta-reading-time::text").re_first(r"\d+")
    )
    notice_data["summary"] = "".join(
            selector.css(".entry-content > p:first-of-type *::text").getall()
        ).strip()
    notice_data["category"] = (
        selector.css(".category-style span.label::text").get()
    )

    return notice_data


# Requisito 5
def get_tech_news(amount):
    url = "https://blog.betrybe.com/"
    notice_data = []
    paginas = amount/12
    contador = 0
    while contador < paginas:
        html = fetch(url)
        url = scrape_next_page_link(html)
        notice_links = scrape_updates(html)

        for link in notice_links:
            notice_html = fetch(link)
            notice_scrape = scrape_news(notice_html)
            notice_data.append(notice_scrape)

        contador += 1
    create_news(notice_data[:amount])
    return notice_data[:amount]

