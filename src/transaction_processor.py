import re
from collections import Counter
from typing import List, Dict, Any


def search_transactions_by_description(transactions: List[Dict[str, Any]], search_string: str) -> List[Dict[str, Any]]:
    try:
        pattern = re.compile(search_string, re.IGNORECASE)
        return [
            transaction for transaction in transactions
            if pattern.search(str(transaction.get('description', '')))
        ]
    except re.error:
        print(f"Ошибка в регулярном выражении: {search_string}")
        return []


def count_transactions_by_category(transactions: List[Dict[str, Any]], categories: Dict[str, List[str]])\
        -> Dict[str, int]:
    transaction_categories = []
    for transaction in transactions:
        description = str(transaction.get('description', '')).upper()
        # Определение категории транзакции
        found_category = None
        for category, keywords in categories.items():
            if any(keyword.upper() in description for keyword in keywords):
                found_category = category
                break
        if found_category:
            transaction_categories.append(found_category)
        else:
            transaction_categories.append("ДРУГОЕ")

    # Использую Counter для подсчета количества транзакций в каждой категории
    category_counts = Counter(transaction_categories)

    # Добавляю категории с нулевым количеством, если они есть в словаре categories
    for category in categories.keys():
        if category not in category_counts:
            category_counts[category] = 0
    return dict(category_counts)
