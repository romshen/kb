from timeit import timeit


def call_recurrently(n):
    """The slowest from listed."""
    return 1 if n < 2 else n * call_recurrently(n - 1)


def iterate_top_down(n):
    result = 1
    counter = n
    while counter > 1:
        result *= counter
        counter -= 1
    return result


def iterate_down_top(n):
    """The fastest from listed."""
    result = 1
    for counter in range(2, n + 1):
        result *= counter
    return result


if __name__ == "__main__":
    print(timeit("call_recurrently(15)", globals=globals()))
    print(timeit("iterate_top_down(15)", globals=globals()))
    print(timeit("iterate_down_top(15)", globals=globals()))

# Other methods suitable for its computation include memoization,[78] dynamic
# programming,[79] and functional programming.[80] The computational complexity
# of these algorithms may be analyzed using the unit-cost random-access machine
# model of computation, in which each arithmetic operation takes constant time
# and each number uses a constant amount of storage space. In this model, these
# methods can compute n! in time O(n), and the iterative version uses space
# O(1).
# Even better efficiency is obtained by computing n! from its prime
# factorization, based on the principle that exponentiation by squaring is
# faster than expanding an exponent into a product.
# the whole algorithm takes time O(n log ^ 2 n), proportional to a single
# multiplication with the same number of bits in its result.
