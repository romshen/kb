import pytest

from algorithms import factorial

test_data = {0: 1, 1: 1, 2: 2, 3: 6, 10: 3628800, 15: 1307674368000}


@pytest.mark.parametrize("test_input,expected", test_data.items())
def test_call_recurrently(test_input, expected):
    assert factorial.call_recurrently(test_input) == expected


@pytest.mark.parametrize("test_input,expected", test_data.items())
def test_iterate_top_down(test_input, expected):
    assert factorial.iterate_top_down(test_input) == expected


@pytest.mark.parametrize("test_input,expected", test_data.items())
def test_factorial_recursion(test_input, expected):
    assert factorial.iterate_down_top(test_input) == expected
