from src.services.processor import process_data


def test_process_data_basic():
    input_data = [1, 2, 3, 4]
    expected = [4, 8]  # Only 2 and 4 doubled are even
    assert process_data(input_data) == expected


def test_process_data_empty():
    assert process_data([]) == []


def test_process_data_all_odd():
    assert process_data([1, 3, 5]) == []
