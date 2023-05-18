from tech_news.database import db
import re


# Requisito 7
def search_by_title(title):
    regex_pattern = re.compile(title, re.IGNORECASE)
    result = db.news.find({"title": regex_pattern})
    return [(notice["title"], notice["url"])for notice in result]


# Requisito 8
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
