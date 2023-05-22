import requests
from time import sleep
from parsel import Selector
from tech_news.database import create_news


# Requisito 1
def fetch(url):
    try:
        response = requests.get(
            url,
            headers={
                "User-agent": "Fake user-agent",
                "Accept": "text/html",
            },
            timeout=3,
        )
    except requests.ReadTimeout:
        return None
    sleep(1)
    if response.status_code and response.status_code == 200:
        return response.text
    return None


# Requisito 2
def scrape_updates(html_content):
    selector = Selector(html_content)
    news_url_list = []

    news_url = selector.css('a.cs-overlay-link::attr(href)').getall()
    news_url_list.extend(news_url)

    return news_url_list


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(html_content)
    next_page = selector.css('a.next.page-numbers::attr(href)').get()
    return next_page


# Requisito 4
def scrape_news(html_content):
    selector = Selector(html_content)

    url = selector.css('link[rel="canonical"]::attr(href)').get()
    title = selector.css('h1::text').get()
    news_date = selector.css('ul.post-meta li.meta-date::text').get()
    writer = selector.css('ul.post-meta a.url.fn.n::text').get()
    read_time = selector.css('ul.post-meta li.meta-reading-time::text').get()
    category = selector.css('div.meta-category span.label::text').get()
    summary = selector.css(
        'div.entry-content > p:first-of-type *::text'
    ).getall()
    clean_summary = ''.join(summary).strip()

    news_data = {
        "url": url,
        "title": title.strip(),
        "timestamp": news_date,
        "writer": writer,
        "reading_time": int(read_time.split(' ')[0]),
        "summary": clean_summary,
        "category": category,
    }
    return news_data


# Requisito 5
def get_tech_news(amount):
    endpoint = 'https://blog.betrybe.com'
    news_url = []

    while endpoint and len(news_url) < amount:
        news = fetch(endpoint)
        fetch_urls = scrape_updates(news)
        news_url.extend(fetch_urls)
        endpoint = scrape_next_page_link(news)

    news_resume = []
    index = 0

    while index < amount:
        news_data = fetch(news_url[index])
        data = scrape_news(news_data)
        news_resume.append(data)
        index += 1

    create_news(news_resume)
    return news_resume


# get_tech_news(6)
