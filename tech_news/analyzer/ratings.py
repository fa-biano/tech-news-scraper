from tech_news.database import find_news


def sort_criteria(element):
    return element[1]


# Requisito 10
def top_5_categories():
    db_news = find_news()
    categories = {}

    for news in db_news:
        if not categories.get(news['category']):
            categories[news['category']] = 0
        categories[news['category']] += 1

    top_categories = [(category, qty) for category, qty in categories.items()]

    sort_top_categories = sorted(top_categories)
    sort_top_categories.sort(key=sort_criteria, reverse=True)

    if len(sort_top_categories) > 5:
        index = 0
        top_5 = []

        while index < 5:
            top_5.append(sort_top_categories[index][0])
            index += 1

        return top_5
    return [category[0] for category in sort_top_categories]
