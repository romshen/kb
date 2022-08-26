class Wrapper(object):
    def __init__(self, func):
        self.call_count = 0
        self.decorated_instance = None
        self.func = func

    def __call__(self, *args, **kwargs):
        self.call_count += 1
        return self.func(self.decorated_instance, *args, **kwargs)

    def __get__(self, obj, objtype):
        self.decorated_instance = obj
        return self


class SomeBase:
    def __init__(self):
        self._model = " World"

    @Wrapper
    async def create(self, arg_1, arg_2):
        return arg_1 + self._model + arg_2


async def test_wrapper():
    base = SomeBase()
    result = await base.create("hello", "!")
    await base.create("hello", "!")

    base2 = SomeBase()
    await base2.create("hello", "!")
    await base2.create("hello", "!")

    assert result == "hello World!"
    assert base.create.call_count == 4
    assert base2.create.call_count == 4
