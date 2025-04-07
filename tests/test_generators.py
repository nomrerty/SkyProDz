import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


def test_filter_by_currency(transactions):
    usd_transactions = list(filter_by_currency(transactions, "USD"))
    assert usd_transactions == [
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229",
        },
    ]
    usd_transactions = list(filter_by_currency(transactions, "RU"))
    assert usd_transactions == []


def test_transaction_descriptions(transactions):
    descriptions = list(transaction_descriptions(transactions))
    assert descriptions == [
        "Перевод со счета на счет",
        "Перевод со счета на счет",
        "Перевод с карты на карту",
        "Перевод организации",
    ]


@pytest.mark.parametrize(
    "start, last, expected",
    [
        (130, 133, ["0000 0000 0000 0130", "0000 0000 0000 0131", "0000 0000 0000 0132", "0000 0000 0000 0133"]),
        (
            120436032,
            120436040,
            [
                "0000 0001 2043 6032",
                "0000 0001 2043 6033",
                "0000 0001 2043 6034",
                "0000 0001 2043 6035",
                "0000 0001 2043 6036",
                "0000 0001 2043 6037",
                "0000 0001 2043 6038",
                "0000 0001 2043 6039",
                "0000 0001 2043 6040",
            ],
        ),
    ],
)
def test_card_number_generator(start, last, expected):
    card_numbers = list(card_number_generator(start, last))
    assert card_numbers == expected
