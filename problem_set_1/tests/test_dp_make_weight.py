import pytest
from problem_set_1.ps1b import dp_make_weight


def test_simple_exact_matches():
    # Basic correctness on simple data
    assert dp_make_weight((1,), 5) == 5  # only 1s
    assert dp_make_weight((1, 2), 4) == 2  # 2+2
    assert dp_make_weight((1, 3, 4), 6) == 2  # 3+3 or 4+1+1? Should pick 3+3


def test_greedy_fails_but_dp_correct():
    # Greedy would pick 4, then 1,1 but DP knows 3 + 3 is better
    assert dp_make_weight((1, 3, 4), 6) == 2


def test_large_target_small_weights():
    assert dp_make_weight((1, 5, 10, 25), 99) == 9
    # 3×25 = 75, 2×10 = 20, 4×1 = 4 → total 9 eggs


def test_memo_not_mutated_between_calls():
    # memo={} default arg is dangerous if code uses it incorrectly
    # This test ensures the result of one call doesn't affect another
    a = dp_make_weight((1, 2), 4)
    b = dp_make_weight((1, 2), 3)
    assert a == 2
    assert b == 2  # should not be influenced by previous call


def test_optimal_for_many_cases():
    # Brute-force expected values for validation
    data = [
        ((1, 2, 4), 7, 3),
        ((1, 2, 4), 11, 4),
        ((1, 3, 4), 9, 3),
        ((1, 5, 12), 17, 2),
    ]
    for weights, target, expected_min in data:
        assert dp_make_weight(weights, target) == expected_min


def test_input_tuple_not_modified():
    egg_weights = (1, 5, 10)
    dp_make_weight(egg_weights, 20)
    assert egg_weights == (1, 5, 10)
