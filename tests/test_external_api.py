from unittest.mock import patch
from src.external_api import convert_to_rub


def test_convert_to_rub_rub_currency():
    """Тест для транзакции в рублях (без конвертации)."""
    transaction = {'amount': 1000.50, 'currency': 'RUB'}
    result = convert_to_rub(transaction)
    assert result == 1000.50


@patch('src.external_api.requests.get')
def test_convert_to_rub_usd(mock_get):
    """Тест конвертации из USD в RUB."""
    mock_get.return_value.json.return_value = {'rates': {'RUB': 90.25}}
    mock_get.return_value.status_code = 200

    transaction = {'amount': 100.00, 'currency': 'USD'}
    result = convert_to_rub(transaction)
    assert result == 9025.00