# a = 'abc'
# a.replace('b', '7')  # replace method returns a copy of string
# print(a)

# ls = [1, 2, 3, 4]
# def fn():
#     ls.append(5)
# fn()
# print(ls)

# 8< ---------------------------------------------------------

# d = dict(('ab', 'cd'))
# print(d)  # {'a': 'b', 'c': 'd'}

# 8< ---------------------------------------------------------
# from timeit import timeit
#
#
# def get_unique_items_iteration_and_checks(items: list) -> list:
#     """
#     Complexity: O(len(items) * len(result))
#     """
#     result = []
#     for n in items:
#         if n not in result:
#             result.append(n)
#     return result
#
#
# def get_unique_items_using_set(items: list) -> list:
#     """
#     Complexity: O(len(items) + len(set))
#     """
#     return list(set(items))
#
#
# def get_unique_items_using_dict(items: list) -> list:
#     """
#     Complexity: O(len(items) + len(dict))
#     """
#     return list(dict.fromkeys(items))
#
#
# def get_unique_items_set_and_list_displays(items: list) -> list:
#     """
#     Complexity: O(len(items) + len(set))
#     This solution is the fastest from listed, because of list and set
#     comprehension.
#     """
#     return [*{*items}]
#
#
# items = [1, 2, 3, 2, 4, 1, 4, 1, 4, 1, 4, 1]
# print(get_unique_items_iteration_and_checks(items))  # [1, 2, 3, 4]
# print(get_unique_items_using_set(items))  # [1, 2, 3, 4]
# print(get_unique_items_using_dict(items))  # [1, 2, 3, 4]
# print(get_unique_items_set_and_list_displays(items))  # [1, 2, 3, 4]

# print(timeit("get_unique_items_iteration_and_checks(items)", globals=globals()))
# print(timeit("get_unique_items_using_dict(items)", globals=globals()))
# print(timeit("get_unique_items_using_set(items)", globals=globals()))
# print(timeit("get_unique_items_set_and_list_displays(items)", globals=globals()))
# 0.9624754799988295
# 0.7738828990004549
# 0.46413010300057067
# 0.4320915860007517

# 8< ---------------------------------------------------------

# hash(0)
# 0
# hash(-1)
# -2
# hash(-2)
# -2
# hash(-3)
# -3

# 8< ---------------------------------------------------------

# x = {'a': 1, 'b': 2}
# y = x
# y['b'] = 7
# x = {3: 9}
# print(x)
# print(y)
# {3: 9}
# {'a': 1, 'b': 7}

# 8< ---------------------------------------------------------

# def fn(a=[], b={}):
#     pass

# ls = [1, 2, ..., n]
# ls.append(999)
# ls.insert(0, 7)

# 8< ---------------------------------------------------------

# class Money:
#     def __init__(self, value: int, currency: str):
#         self.value = value
#         self.currency = currency
#
#     def __add__(self, b):
#         return Money(self.value + b.value, 'USD')
#
#
# Money(2, 'USD') + Money(5, 'USD') = Money(7, 'USD')
#
# Money(2, 'USD') + Money(7, 'EUR')
# Money(7, 'EUR') - Money(2, 'USD')

# 8< ---------------------------------------------------------

# class One:
#     pass
#
# print(One == One)  # True
# a = One()
# b = One()
# print(a == b)  # False

# 8< ---------------------------------------------------------
