import pytest
from typing import List
from src.processing import filter_by_state, sort_by_date

data = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "CANCELED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]

@pytest.mark.parametrize(
    "input, expected",
    [
        (
            data,
            [
                {
                    "id": 41428829,
                    "state": "EXECUTED",
                    "date": "2019-07-03T18:35:29.512364",
                }
            ],
        ),
        (
            [
                {"id": 1, "state": "PENDING", "date": "2021-01-01T00:00:00"},
                {"id": 2, "state": "EXECUTED", "date": "2021-01-02T00:00:00"},
            ],
            [
                {"id": 2, "state": "EXECUTED", "date": "2021-01-02T00:00:00"},
            ],
        ),
    ],
)
def test_filter_state(input: List[dict], expected: List[dict]) -> None:
    assert filter_by_state(input) == expected

def test_sort_by_date() -> None:
    sorted_data = [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 939719570, "state": "CANCELED", "date": "2018-06-30T02:08:58.425572"},
    ]
    assert sort_by_date(data) == sorted_data

def test_sort_by_date_ascending() -> None:
    sorted_data_ascending = [
        {"id": 939719570, "state": "CANCELED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    ]
    assert sort_by_date(data, sort_order=False) == sorted_data_ascending
