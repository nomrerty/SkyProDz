import pytest
from unittest.mock import patch, mock_open
import pandas as pd
from src.transactions import load_transactions_from_csv, load_transactions_from_excel

# Тестовые данные
CSV_MOCK_DATA = """id;state;amount
1;EXECUTED;100
2;PENDING;200"""

EXCEL_MOCK_DATA = [
    {"id": 1, "state": "EXECUTED", "amount": 100},
    {"id": 2, "state": "PENDING", "amount": 200}
]

def test_load_transactions_from_csv_success():
    """Тест успешной загрузки CSV."""
    with patch("builtins.open", mock_open(read_data=CSV_MOCK_DATA)):
        with patch("pandas.read_csv") as mock_read_csv:
            mock_read_csv.return_value = pd.DataFrame(EXCEL_MOCK_DATA)
            result = load_transactions_from_csv()
            assert len(result) == 2
            assert result[0]["state"] == "EXECUTED"

def test_load_transactions_from_csv_error():
    """Тест ошибки при загрузке CSV."""
    with patch("pandas.read_csv", side_effect=Exception("File not found")):
        result = load_transactions_from_csv("invalid_path.csv")
        assert result == []

def test_load_transactions_from_excel_success():
    """Тест успешной загрузки Excel."""
    with patch("pandas.read_excel") as mock_read_excel:
        mock_read_excel.return_value = pd.DataFrame(EXCEL_MOCK_DATA)
        result = load_transactions_from_excel()
        assert len(result) == 2
        assert result[1]["state"] == "PENDING"

def test_load_transactions_from_excel_error():
    """Тест ошибки при загрузке Excel."""
    with patch("pandas.read_excel", side_effect=Exception("File not found")):
        result = load_transactions_from_excel("invalid_path.xlsx")
        assert result == []
