import re
from collections import Counter
from typing import List, Dict, Any


def search_transactions_by_description(transactions: List[Dict[str, Any]], search_string: str) -> List[Dict[str, Any]]:
    pattern = re.compile(search_string, re.IGNORECASE)
    return [
        transaction for transaction in transactions
        if 'description' in transaction and pattern.search(transaction['description'])
    ]


def count_transactions_by_category(transactions: List[Dict[str, Any]], categories: List[str]) -> Dict[str, int]:
    descriptions = [
        transaction.get('description', '').upper()
        for transaction in transactions
    ]
    
    category_counts = Counter(descriptions)
    return {
        category: category_counts.get(category, 0)
        for category in categories
    } 