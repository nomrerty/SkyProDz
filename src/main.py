import json 
import csv
import pandas as pd
import os
from typing import List, Dict, Any
from src.transaction_processor import search_transactions_by_description


def format_transaction(transaction: Dict[str, Any]) -> str:
    date = transaction.get('date', '')
    description = transaction.get('description', '')
    
    if 'operationAmount' in transaction:
        amount = transaction['operationAmount'].get('amount', '')
        currency = transaction['operationAmount'].get('currency', {}).get('name', '')
    else:
        amount = transaction.get('amount', '')
        currency = transaction.get('currency_name', '')
    
    from_account = transaction.get('from', '')
    to_account = transaction.get('to', '')
    
    if from_account and to_account:
        account_info = f"{from_account} -> {to_account}"
    elif to_account:
        account_info = to_account
    else:
        account_info = ''
        
    return f"{date} {description}\n{account_info}\nСумма: {amount} {currency}\n"


def normalize_transaction(transaction: Dict[str, Any]) -> Dict[str, Any]:
    """Приводит транзакцию к единому формату независимо от источника данных."""
    # Преобразуем числовые значения в строки
    for key, value in transaction.items():
        if isinstance(value, (int, float)):
            transaction[key] = str(value)
            
    if 'operationAmount' not in transaction and 'amount' in transaction:
        transaction['operationAmount'] = {
            'amount': transaction['amount'],
            'currency': {
                'name': transaction.get('currency_name', ''),
                'code': transaction.get('currency_code', '')
            }
        }
    return transaction


def load_transactions(file_path: str, file_type: str) -> List[Dict[str, Any]]:
    try:
        if file_type == 'json':
            with open(file_path, 'r', encoding='utf-8') as file:
                return json.load(file)
        elif file_type == 'csv':
            with open(file_path, 'r', encoding='utf-8') as file:
                reader = csv.DictReader(file, delimiter=';')
                transactions = list(reader)
                return [normalize_transaction(t) for t in transactions]
        elif file_type == 'xlsx':
            df = pd.read_excel(file_path)
            transactions = df.to_dict('records')
            return [normalize_transaction(t) for t in transactions]
    except Exception as e:
        print(f"Ошибка при загрузке файла: {e}")
        return []
    return []


def main():
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    
    while True:
        print("\nВыберите необходимый пункт меню:")
        print("1. Получить информацию о транзакциях из JSON-файла")
        print("2. Получить информацию о транзакциях из CSV-файла")
        print("3. Получить информацию о транзакциях из XLSX-файла")
        
        choice = input().strip()
        if choice not in ['1', '2', '3']:
            print("Неверный выбор. Пожалуйста, выберите 1, 2 или 3.")
            continue
            
        file_type = {
            '1': 'json',
            '2': 'csv',
            '3': 'xlsx'
        }[choice]
        
        print(f"Для обработки выбран {file_type.upper()}-файл.")
        
        file_paths = {
            'json': 'data/operations.json',
            'csv': 'data/transactions.csv',
            'xlsx': 'data/transactions_excel.xlsx'
        }
        
        transactions = load_transactions(file_paths[file_type], file_type)
        if not transactions:
            print("Не удалось загрузить файл с транзакциями")
            continue
        
        valid_statuses = ['EXECUTED', 'CANCELED', 'PENDING']
        while True:
            print("\nВведите статус, по которому необходимо выполнить фильтрацию.")
            print("Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING")
            status = input().strip().upper()
            
            if status not in valid_statuses:
                print(f'Статус операции "{status}" недоступен.')
                continue
            break
            
        filtered_transactions = [
            t for t in transactions
            if t.get('state', '').upper() == status
        ]
        
        print(f'Операции отфильтрованы по статусу "{status}"')
        
        if input("\nОтсортировать операции по дате? Да/Нет: ").strip().lower() == 'да':
            sort_order = input("Отсортировать по возрастанию или по убыванию? ").strip().lower()
            reverse = sort_order == 'по убыванию'
            filtered_transactions.sort(key=lambda x: x.get('date', ''), reverse=reverse)
        
        if input("\nВыводить только рублевые транзакции? Да/Нет: ").strip().lower() == 'да':
            filtered_transactions = [
                t for t in filtered_transactions
                if (t.get('operationAmount', {}).get('currency', {}).get('name') == 'руб.' or
                    t.get('currency_name') == 'руб.')
            ]
        
        if input("\nОтфильтровать список транзакций по определенному слову в описании? Да/Нет: ").strip().lower() == 'да':
            search_term = input("Введите слово для поиска: ").strip()
            filtered_transactions = search_transactions_by_description(filtered_transactions, search_term)
        
        print("\nРаспечатываю итоговый список транзакций...")
        print(f"\nВсего банковских операций в выборке: {len(filtered_transactions)}\n")
        
        if not filtered_transactions:
            print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
        else:
            for transaction in filtered_transactions:
                print(format_transaction(transaction))
        
        if input("\nХотите выполнить еще одну операцию? Да/Нет: ").strip().lower() != 'да':
            break
    
    print("Спасибо за использование программы!")


if __name__ == "__main__":
    main() 