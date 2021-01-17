from typing import List


def list_to_string(list: List[int], separator: str) -> int:
    """Convert list to string

    Args:
        list (List[int]): list with integers
        separator (str): [description]
    Returns:
        str: list splitted by space
    """
    return separator.join(map(str, list))
