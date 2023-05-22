from tech_news.database import find_news
import datetime


# Requisito 7
def search_by_title(title):
    db_news = find_news()
    filterd_news = [
        (news['title'], news['url'])
        for news in db_news
        if title.lower() in news['title'].lower()
    ]

    return filterd_news


# Requisito 8
def search_by_date(date):
    try:
        datetime.date.fromisoformat(date)
    except ValueError:
        raise ValueError('Data inválida')

    db_news = find_news()
    filterd_news = []

    for news in db_news:
        db_date = news['timestamp'].split('/')
        format_date = datetime.datetime(
            int(db_date[2]),
            int(db_date[1]),
            int(db_date[0]),
        ).strftime("%Y-%m-%d")
        if date == format_date:
            filterd_news.append((news['title'], news['url']))

    return filterd_news


# Requisito 9
def search_by_category(category):
    db_news = find_news()
    filterd_news = [
        (news['title'], news['url'])
        for news in db_news
        if category.lower() in news['category'].lower()
    ]

    return filterd_news
