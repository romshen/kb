import pytest

from algorithms import fibonacci

input_output_mapping = {
    0: 0,
    1: 1,
    2: 1,
    3: 2,
    4: 3,
    5: 5,
}


@pytest.mark.parametrize("test_input,expected", input_output_mapping.items())
def test_fib_1(test_input, expected):
    assert fibonacci.fib_1(test_input) == expected


@pytest.mark.parametrize("test_input,expected", input_output_mapping.items())
def test_fib_2(test_input, expected):
    assert fibonacci.fib_2(test_input) == expected


@pytest.mark.parametrize("test_input,expected", input_output_mapping.items())
def test_fib_3(test_input, expected):
    assert fibonacci.fib_3(test_input) == expected


@pytest.mark.parametrize("test_input,expected", input_output_mapping.items())
def test_fib_4(test_input, expected):
    assert fibonacci.fib_4(test_input) == expected


@pytest.mark.parametrize("test_input,expected", input_output_mapping.items())
def test_fib_5(test_input, expected):
    assert fibonacci.fib_5(test_input) == expected
