from problem_set_1.ps1a import brute_force_cow_transport


def test_basic_valid_input():
    cows = {"A": 3, "B": 5, "C": 2}
    result = brute_force_cow_transport(cows, limit=10)
    # Only one trip needed
    assert len(result) == 1
    assert sorted(result[0]) == ["A", "B", "C"]


def test_multiple_trips():
    cows = {"A": 9, "B": 9, "C": 2}
    result = brute_force_cow_transport(cows, limit=10)
    assert len(result) == 3  # A alone, B alone, C alone


def test_empty_dict():
    assert brute_force_cow_transport({}) == []
