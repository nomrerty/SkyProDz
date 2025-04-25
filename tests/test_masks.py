import pytest

from src.masks import get_mask_account, get_mask_card_number


def test_get_mask_card_number(masks_card_1, masks_card_2):
    assert get_mask_card_number(7000792289606361) == masks_card_1
    assert get_mask_card_number("7000792289606361") == masks_card_1

@pytest.mark.parametrize(
    "num,expected",
    [
        ("", "Некорректный номер карты, пожалуйста введите верный номер карты"),
        (1.2, "Некорректный номер карты, пожалуйста введите верный номер карты"),
        ("        7000792289606361       ", "7000 79** **** 6361"),
        ("        7 0 0 0 7 9 2 2 8 9 6 0 6 3 6 1        ", "7000 79** **** 6361"),
        ("        1023456789101112       ", "1023 45** **** 1112"),
        ("        1 0 2 3 4 5 6 7 8 9 1 0 1 1 1 2        ", "1023 45** **** 1112"),
        (" ", "Некорректный номер карты, пожалуйста введите верный номер карты"),
        (
            "123456789123456789",
            "Некорректный номер карты, пожалуйста введите верный номер карты",
        ),
    ],
)
def test_get_mask_card_number_parametrize(num, expected):
    assert get_mask_card_number(num) == expected


@pytest.mark.parametrize(
    "num,expected",
    [
        ("12345678901234567890", "**7890"),
        (12345678901234567890, "**7890"),
        ("123", "Некорректный номер счета"),
        ("", "Некорректный номер счета"),
    ],
)
def test_get_mask_account(num, expected):
    assert get_mask_account(num) == expected