from typing import List


def filter_by_state(list_of_dicts: List[dict], state: str = "EXECUTED") -> List[dict]:
    return [item for item in list_of_dicts if item.get("state") == state]


def sort_by_date(list_of_dicts: List[dict], sort_order: bool = True) -> List[dict]:
    return sorted(list_of_dicts, key=lambda x: x.get("date"), reverse=sort_order)
