import pandas as pd
from typing import List, Dict
import os


def get_csv_path() -> str:
    """Возвращает абсолютный путь к CSV-файлу."""
    base_dir = os.path.dirname(os.path.dirname(__file__))  # Папка проекта
    return os.path.join(base_dir, "test_data", "test_transactions.csv")


def get_excel_path() -> str:
    """Возвращает абсолютный путь к Excel-файлу."""
    base_dir = os.path.dirname(os.path.dirname(__file__))  # Папка проекта
    return os.path.join(base_dir, "test_data", "test_transactions.xlsx")


def load_transactions_from_csv(file_path: str = None) -> List[Dict]:
    """Загружает транзакции из CSV."""
    path = file_path or get_csv_path()  # Использует переданный путь или путь по умолчанию
    try:
        df = pd.read_csv(path, sep=';')
        return df.to_dict('records')
    except Exception as e:
        print(f"Ошибка при чтении CSV: {e}")
        return []


def load_transactions_from_excel(file_path: str = None) -> List[Dict]:
    """Загружает транзакции из Excel."""
    path = file_path or get_excel_path()  # Использует переданный путь или путь по умолчанию
    try:
        df = pd.read_excel(path, engine='openpyxl')
        return df.to_dict('records')
    except Exception as e:
        print(f"Ошибка при чтении Excel: {e}")
        return []
