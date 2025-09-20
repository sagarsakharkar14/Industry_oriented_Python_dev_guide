def process_data(data: list[int]) -> list[int]:
    """
    Doubles each number in the list and returns only even results.
    """
    return [x * 2 for x in data if (x * 2) % 2 == 0]
