"""
The objective is to count instance method calls with class decorator.
I chose the class decorator, because want to store there field call_count
separately for every decorated instance method. A function decorator can't
solve this problem because either developer should manually add fields
call_count to the class with decorated methods or add to the decorator function
 an attribute field call_count. The first case don't follow OOP paradigm and
 also there is extra work. At the second case function attribute keep count of
 all decorated instance methods (multiply amount of instances on amount of
 decorated methods). At result, I want to get call count like this:
 instance_name.method_name.call_count.
"""
from functools import wraps


def call_count(function):
    @wraps(function)
    async def new_function(self, *args, **kwargs):
        if new_function.count.get(function.__name__):
            new_function.count[function.__name__] += 1
        else:
            new_function.count[function.__name__] = 1

        return await function(self, *args, **kwargs)

    new_function.count = {}
    return new_function


def call_count2(function):
    @wraps(function)
    async def new_function(self, *args, **kwargs):
        setattr(
            new_function,
            function.__name__,
            getattr(new_function, function.__name__) + 1,
        )

        return await function(self, *args, **kwargs)

    setattr(new_function, function.__name__, 0)
    return new_function


class CallCount:
    def __init__(self, function_name):
        self._field_name = f"_{function_name}_call_count"
        setattr(self, self._field_name, 0)

    @property
    def amount(self):
        return getattr(self, self._field_name)

    @amount.setter
    def amount(self, increment):
        setattr(self, self._field_name, increment)

    @staticmethod
    def bind(function):
        @wraps(function)
        async def new_function(self, *args, **kwargs):
            new_function.call_count.amount += 1
            return await function(self, *args, **kwargs)

        new_function.call_count = CallCount(function.__name__)
        return new_function


async def test_call_count():
    class SomeBase:
        def __init__(self):
            self._model = " World"

        @call_count
        async def create(self, arg_1, arg_2):
            return arg_1 + self._model + arg_2

        @call_count
        async def update(self, arg_1, arg_2):
            return arg_1 + self._model + arg_2

    base = SomeBase()
    result = await base.create("hello", "!")
    await base.update("hello", "!")

    class SomeBase2(SomeBase):
        pass

    base2 = SomeBase2()
    result2 = await base2.create("hello", "!")
    await base2.update("hello", "!")
    print(f"{base.create.count=}")

    assert result == "hello World!"
    assert result2 == "hello World!"
    assert base.create.count[base.create.__name__] == 2
    assert base2.update.count[base2.update.__name__] == 2


async def test_call_count2():
    class SomeBase:
        def __init__(self):
            self._model = " World"

        @call_count2
        async def create(self, arg_1, arg_2):
            return arg_1 + self._model + arg_2

        @call_count2
        async def update(self, arg_1, arg_2):
            return arg_1 + self._model + arg_2

    base = SomeBase()
    result = await base.create("hello", "!")
    await base.update("hello", "!")

    class SomeBase2(SomeBase):
        pass

    base2 = SomeBase2()
    result2 = await base2.create("hello", "!")
    await base2.update("hello", "!")
    print(f"{base.create.create=}")

    assert result == "hello World!"
    assert result2 == "hello World!"
    assert base.create.create == 2
    assert base2.update.update == 2


async def test_call_count3():
    class SomeBase:
        def __init__(self):
            self._model = " World"

        @CallCount.bind
        async def create(self, arg_1, arg_2):
            return arg_1 + self._model + arg_2

        @CallCount.bind
        async def update(self, arg_1, arg_2):
            return arg_1 + self._model + arg_2

    base = SomeBase()
    result = await base.create("hello", "!")
    await base.update("hello", "!")

    class SomeBase2(SomeBase):
        pass

    base2 = SomeBase2()
    result2 = await base2.create("hello", "!")
    await base2.update("hello", "!")

    assert result == "hello World!"
    assert result2 == "hello World!"
    assert base.create.call_count.amount == 2
    assert base2.create.call_count.amount == 2
    assert base.update.call_count.amount == 2
    assert base2.update.call_count.amount == 2
