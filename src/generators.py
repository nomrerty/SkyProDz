def filter_by_currency(transactions, currency):
    """Возвращает итератор с транзакциями, где валюта соответствует заданной."""
    return filter(
        lambda transaction: transaction.get("operationAmount", {}).get("currency", {}).get("code") == currency
        or transaction.get("currency_code") == currency,
        transactions,
    )


def transaction_descriptions(transactions):
    """Генерирует описания транзакций."""
    for tran in transactions:
        if tran:  # Проверка на пустой словарь
            yield tran.get("description")


def card_number_generator(start, last):
    """Генерирует номера карт в заданном диапазоне."""

    def format_card_number(number):
        """Форматирует номер карты в стандартный формат XXXX XXXX XXXX XXXX."""
        string = f"{number:016}"
        return " ".join([string[i : i + 4] for i in range(0, len(string), 4)])

    while start <= last:
        yield format_card_number(start)
        start += 1
