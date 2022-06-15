import pytest

from algorithms import armstorng_numbers

test_data = {1: True, 153: True}


@pytest.mark.parametrize("test_input,expected", test_data.items())
def test_is_armstorng_number_1_positive(test_input, expected):
    assert armstorng_numbers.is_armstorng_number_1(test_input) is expected


def test_is_armstorng_number_1_negative():
    assert armstorng_numbers.is_armstorng_number_1(10) is False


@pytest.mark.parametrize("test_input,expected", test_data.items())
def test_is_armstorng_number_2_positive(test_input, expected):
    assert armstorng_numbers.is_armstorng_number_2(test_input) is expected


def test_is_armstorng_number_2_negative():
    assert armstorng_numbers.is_armstorng_number_2(10) is False


@pytest.mark.parametrize("test_input,expected", test_data.items())
def test_is_armstorng_number_3_positive(test_input, expected):
    assert armstorng_numbers.is_armstorng_number_3(test_input) is expected


def test_is_armstorng_number_3_negative():
    assert armstorng_numbers.is_armstorng_number_3(10) is False
