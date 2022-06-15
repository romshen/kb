from timeit import timeit


def is_armstorng_number_1(n):
    """String casting approach."""
    s = str(n)
    length = len(s)

    _sum = 0
    for i in range(length):
        _sum += int(s[i]) ** length

    return n == _sum


def count_digits(n):
    length = 0
    remainder = n
    while remainder > 0:
        length += 1
        remainder //= 10
    return length


def is_armstorng_number_2(n):
    """Math approach. Faster than string casting."""
    length = count_digits(n)

    _sum = 0
    remainder = n
    while remainder > 0:
        _sum += (remainder % 10) ** length
        remainder //= 10

    return n == _sum


def is_armstorng_number_3(n):
    """Log approach.
    This function is slowest because of import of math module.
    If we move it at the top level this function the fastest."""
    from math import floor, log10

    length = floor(log10(n) + 1)

    _sum = 0
    remainder = n
    while remainder > 0:
        _sum += (remainder % 10) ** length
        remainder //= 10

    return n == _sum


def filter_n_armstorng_numbers(n, max=1000000):
    amount = n
    number = 0
    while amount > 0:
        if is_armstorng_number_2(number):
            print(number)
            amount -= 1
        number += 1


filter_n_armstorng_numbers(13)


def print_armstorng_numbers_in_range(n):
    armstrong_nunbers = tuple(filter(is_armstorng_number_2, range(n + 1)))
    print(*armstrong_nunbers)


print_armstorng_numbers_in_range(153)


if __name__ == "__main__":
    print(timeit("is_armstorng_number_string_casting(153)", globals=globals()))
    print(timeit("is_armstorng_number_math_approach(153)", globals=globals()))
    print(timeit("is_armstorng_number_log_approach(153)", globals=globals()))
