import os
import requests
from dotenv import load_dotenv

load_dotenv()

EXCHANGE_API_KEY = os.getenv('EXCHANGE_API_KEY')
EXCHANGE_API_URL = 'https://api.apilayer.com/exchangerates_data/latest'


def get_exchange_rate(base_currency: str, target_currency: str = 'RUB') -> float:
    """Получает текущий курс обмена валюты через Exchange Rates Data API."""
    headers = {'apikey': EXCHANGE_API_KEY}
    params = {'base': base_currency, 'symbols': target_currency}

    try:
        response = requests.get(EXCHANGE_API_URL, headers=headers, params=params)
        response.raise_for_status()
        data = response.json()
        return data['rates'][target_currency]
    except requests.RequestException as e:
        raise Exception(f"Ошибка при получении курса валют: {str(e)}")


def convert_to_rub(transaction: dict) -> float:
    """Конвертирует сумму транзакции в рубли."""
    amount = float(transaction['amount'])
    currency = transaction['currency']

    if currency == 'RUB':
        return amount

    if currency not in ['USD', 'EUR']:
        raise ValueError(f"Неподдерживаемая валюта: {currency}")

    rate = get_exchange_rate(currency)
    return round(amount * rate, 2)
