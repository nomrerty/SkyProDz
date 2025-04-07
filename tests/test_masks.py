import sys

from src.masks import mask_account, mask_card

sys.path.append("/")


""" # Проверка функции mask_card() с аннотациями типов """


def test_mask_card(card_numbers) -> None:
    assert mask_card(card_numbers[0]) == "2135 42** **** 3546"
    assert mask_card(card_numbers[1]) == "Некорректный номер карты"


""" # Проверка функции mask_account() с аннотациями типов """


def test_mask_account(accounts) -> None:
    assert mask_account(accounts[0]) == "**4305"
    assert mask_account(accounts[1]) == "Некорректный номер счета"
    assert mask_account(accounts[2]) == "**7463"
    assert mask_account(accounts[3]) == "Некорректный номер счета"


""" # Проверка функции mask_account() с аннотациями типов """
