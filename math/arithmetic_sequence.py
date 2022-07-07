# Task: sum up the terms of this arithmetic sequence [1, 2, 3, ..., 98, 99, 100]
from timeit import timeit

# option 1
print(timeit("sum((number for number in range(1, 10001)))", number=1000))

# option 2
print(
    timeit(
        "from functools import reduce;"
        "reduce(lambda a, b: a + b, (number for number in range(1, 10001)))",
        number=1000,
    )
)

# option 3
# formula S = (n/2) × (2a + (n−1)d), where
# a - the first term;
# d - the "common difference" between terms;
# n - how many terms to add up.

print(timeit("5000 * (2 + 9999)", number=1000))
