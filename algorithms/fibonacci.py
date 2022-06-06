from timeit import timeit
from math import sqrt


def cash(fun):
    cache = {}

    def memoize(*args, **kwargs):
        if args in cache:
            return cache[args]
        result = fun(*args, **kwargs)
        cache[args] = result
        return result

    return memoize


# @cash
def fib_1(n):
    """
    Time Complexity:O(n)
    Extra Space: O(1)
    """
    if n < 2:
        return n
    a, b = 0, 1
    for _ in range(1, n):
        result = a + b
        a = b
        b = result

    return  result


# @cash
def fib_2(n):
    """The best approach without caching."""
    if n < 2:
        return n
    a, b = 0, 1
    for _ in range(1, n):
        a, b = b, a + b

    return  b


# @cash
def fib_3(n):
    """The worst and slowest approach.
    Runtime complexity: O(ϕn), where ϕ is the golden ratio (ϕ≃1.618...)
    Space complexity: O(n)
    """
    if n < 2:
        return n

    return fib_3(n - 2) + fib_3(n - 1)


# @cash
def fib_4(n):
    """
    Runtime complexity: O(n)
    Space complexity: O(n)
    """
    f = [0, 1]
    for i in range(2, n + 1):
        f.append(f[i - 1] + f[i - 2])
    return f[n]


def fib_5(n):
    """
    In this method we directly implement the formula for nth term in the fibonacci series.
    Fn = {[(√5 + 1)/2] ^ n} / √5
    Time Complexity: O(logn), this is because calculating phi^n takes logn time
    Space Complexity: O(1)
    Reference: http://www.maths.surrey.ac.uk/hosted-sites/R.Knott/Fibonacci/fibFormula.html
    """
    square_root_five = sqrt(5)
    return round(pow((square_root_five + 1) / 2, n) / square_root_five)


# test functions above
input_output_mapping = {
    0: 0,
    1: 1,
    2: 1,
    3: 2,
    4: 3,
    5: 5,
}


def test_fib(*functions):
    for func in functions:
        for k, v in input_output_mapping.items():
            assert func(k) == v


test_fib(fib_1, fib_2, fib_3, fib_4, fib_5)


# check time of completion
for n in range(1, 6):
    print(timeit(f'fib_{n}(5)', globals=globals()))
