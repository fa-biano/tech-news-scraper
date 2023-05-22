import sys
from tech_news.scraper import get_tech_news
from tech_news.analyzer.search_engine import search_by_title, search_by_date,\
    search_by_category
from tech_news.analyzer.ratings import top_5_categories


# Requisitos 11 e 12
def analyzer_menu():
    menu_options = input(
        'Selecione uma das opções a seguir:\n'
        ' 0 - Popular o banco com notícias;\n'
        ' 1 - Buscar notícias por título;\n'
        ' 2 - Buscar notícias por data;\n'
        ' 3 - Buscar notícias por categoria;\n'
        ' 4 - Listar top 5 categorias;\n'
        ' 5 - Sair.\n'
    )

    # just to handle linter import error
    features = {
        '0': get_tech_news,
        '1': search_by_title,
        '2': search_by_date,
        '3': search_by_category,
        '4': top_5_categories,
        '5': print,
    }

    features = {
        '0': "get_tech_news(int(input('Digite quantas notícias serão \
            buscadas: ')))",
        '1': "search_by_title(input('Digite o título: '))",
        '2': "search_by_date(input('Digite a data no formato aaaa-mm-dd: '))",
        '3': "search_by_category(input('Digite a categoria: '))",
        '4': "top_5_categories()",
        '5': "print('Encerrando script')",
    }

    try:
        return eval(features[menu_options])
    except KeyError:
        sys.stderr.write('Opção inválida\n')
