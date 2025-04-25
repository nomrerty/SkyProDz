from typing import Any, List

def filter_by_state(list_of_dicts: List[dict], state: str = "EXECUTED") -> List[dict]:
    """Проверяет значение в словарях на заданное и если оно совпадает то, выводит его"""
    return [item for item in list_of_dicts if item.get("state") == state]

def sort_by_date(list_of_dicts: List[dict], sort_order: bool = True) -> List[dict]:
    """Сортирует список по датам в словарях по убыванию (по умолчанию)"""
    return sorted(list_of_dicts, key=lambda x: x.get("date"), reverse=sort_order)
