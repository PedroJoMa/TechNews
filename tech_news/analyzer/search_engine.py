from tech_news.database import db
import re
from datetime import datetime


# Requisito 7
def search_by_title(title):
    regex_pattern = re.compile(title, re.IGNORECASE)
    result = db.news.find({"title": regex_pattern})
    return [(notice["title"], notice["url"])for notice in result]


# Requisito 8
def search_by_date(date):
    try:
        convert_date = datetime.strptime(date, "%Y-%m-%d").strftime("%d/%m/%Y")
        response = db.news.find({
            "timestamp": convert_date
        })
        return [(notice["title"], notice["url"])for notice in response]
    except ValueError:
        raise ValueError("Data inválida")


# Requisito 9
def search_by_category(category):
    search_filter = re.compile(category, re.IGNORECASE)
    response = db.news.find({
        "category": search_filter
    })
    return [(notice["title"], notice["url"])for notice in response]

