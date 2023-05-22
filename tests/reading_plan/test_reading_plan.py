import pytest
from unittest.mock import patch
from tech_news.analyzer.reading_plan import ReadingPlanService  # noqa: F401, E261, E501

MOCKED_NEWS = [
    {
        "url": 'url.1',
        "title": 'Titulo 1',
        "timestamp": '08/07/2022',
        "writer": 'escritor 1',
        "reading_time": 3,
        "summary": 'resumo 1',
        "category": 'category',
    },
    {
        "url": 'url.2',
        "title": 'Titulo 2',
        "timestamp": '08/07/2022',
        "writer": 'escritor 2',
        "reading_time": 4,
        "summary": 'resumo 2',
        "category": 'category',
    },
    {
        "url": 'url.3',
        "title": 'Titulo 3',
        "timestamp": '08/07/2022',
        "writer": 'escritor 3',
        "reading_time": 10,
        "summary": 'resumo 3',
        "category": 'category',
    },
]


def test_reading_plan_group_news():
    error_string = "Valor 'available_time' deve ser maior que zero"
    with pytest.raises(ValueError, match=error_string):
        ReadingPlanService().group_news_for_available_time(-1)

    mocked_method = 'tech_news.analyzer.reading_plan.find_news'
    with patch(mocked_method, return_value=MOCKED_NEWS):
        response = ReadingPlanService().group_news_for_available_time(8)
        expect = {
            "readable": [
                {
                    "unfilled_time": 1,
                    "chosen_news": [
                        ("Titulo 1", 3),
                        ("Titulo 2", 4),
                    ],
                },
            ],
            "unreadable": [
                ("Titulo 3", 10),
            ],
        }

        assert response == expect
