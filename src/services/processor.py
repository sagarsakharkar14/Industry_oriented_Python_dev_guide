from src.utils.helpers import log


def process_data(data: list[int]) -> list[int]:
    """
    Doubles each number in the list and returns only even results.
    """
    log(f"Processing data: {data}")
    return [x * 2 for x in data if (x) % 2 == 0]
