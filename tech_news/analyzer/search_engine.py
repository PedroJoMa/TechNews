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
    # regex_pattern = r"\d{4}-\d{2}-\d{2}"
    # if not re.match(regex_pattern, date):
    #     ValueError("Data inválida")
    # formated_date = f"{date[8:10]}/{date[5:7]}/{date[0:4]}"
    # response = db.news.find({
    #     "timestamp": formated_date
    # })
    # return [(notice["title"], notice["url"])for notice in response]
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
    """Seu código deve vir aqui"""
