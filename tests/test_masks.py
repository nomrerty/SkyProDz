from src.masks import mask_account, mask_card

"""
# Проверка функции mask_card() с аннотациями типов
"""


def test_mask_card() -> None:
    assert mask_card("2135421354213546") == "2135 46** **** 3546"
    assert mask_card("21354") == "Некорректный номер карты"


"""
# Проверка функции mask_account() с аннотациями типов
"""


def test_mask_account() -> None:
    assert mask_account("73654108430135874305") == "**4305"
    assert mask_account("123") == "Некорректный номер счета"
