import pytest
import copy
from problem_set_1.ps1a import greedy_cow_transport

def test_simple_case():
    cows = {
        "Betsy": 6,
        "MooMoo": 5,
        "Tiny": 3,
    }
    result = greedy_cow_transport(cows, limit=10)

    # Largest cow (6) + smallest that fits (3) = 9, so Tiny goes with Betsy
    # Remaining is MooMoo (5)
    assert result == [["Betsy", "Tiny"], ["MooMoo"]]


def test_greedy_bad_input_type():
    # Strings, lists, tuples, ints — all invalid
    bad_inputs = ["not a dict", 42, ["cow"], (1, 2), None]

    for bad in bad_inputs:
        with pytest.raises(TypeError):
            greedy_cow_transport(bad)


def test_exact_fit():
    cows = {
        "A": 5,
        "B": 5,
        "C": 10
    }
    result = greedy_cow_transport(cows, limit=10)

    # C takes its own trip (10)
    # A + B = 10
    assert result == [["C"], ["A", "B"]]


def test_no_mutation():
    cows = {
        "A": 8,
        "B": 2,
        "C": 7,
    }
    cows_copy = copy.deepcopy(cows)

    _ = greedy_cow_transport(cows, limit=10)

    assert cows == cows_copy, "Function should NOT mutate input dictionary"


def test_one_cow_per_trip():
    cows = {
        "A": 9,
        "B": 9,
        "C": 9,
    }
    result = greedy_cow_transport(cows, limit=10)

    # Every cow is too big to share a trip
    assert result == [["A"], ["B"], ["C"]]


def test_large_to_small_ordering():
    cows = {
        "Big": 8,
        "Medium": 5,
        "Small": 2
    }
    result = greedy_cow_transport(cows, limit=10)


    assert result == [["Big", "Small"], ["Medium"]]


def test_empty_input():
    result = greedy_cow_transport({}, limit=10)
    assert result == [], "Empty input should return empty schedule"