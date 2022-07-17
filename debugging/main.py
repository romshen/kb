def multiply(x, y):
    return x * y


def calculate(x, y):
    y = multiply(y, 10)
    x = sum((x, 3))
    return sum((x, y))


x = 20
y = 50
breakpoint()
x = x + 10
out = calculate(x, y)
