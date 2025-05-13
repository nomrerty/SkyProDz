import re
from collections import Counter
from typing import List, Dict, Any


def search_transactions_by_description(transactions: List[Dict[str, Any]], search_string: str) -> List[Dict[str, Any]]:
    """
    Search transactions by description using regular expressions.
    
    Args:
        transactions: List of transaction dictionaries
        search_string: String to search for in descriptions
        
    Returns:
        List of transactions matching the search string
    """
    pattern = re.compile(search_string, re.IGNORECASE)
    return [
        transaction for transaction in transactions
        if 'description' in transaction and pattern.search(transaction['description'])
    ]


def count_transactions_by_category(transactions: List[Dict[str, Any]], categories: List[str]) -> Dict[str, int]:
    """
    Count transactions by category.
    
    Args:
        transactions: List of transaction dictionaries
        categories: List of categories to count
        
    Returns:
        Dictionary with category counts
    """
    descriptions = [
        transaction.get('description', '').upper()
        for transaction in transactions
    ]
    
    category_counts = Counter(descriptions)
    return {
        category: category_counts.get(category, 0)
        for category in categories
    } 