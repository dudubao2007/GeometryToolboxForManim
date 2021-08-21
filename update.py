def uvalue(x):
    if getattr(x, "uvalue", None) is not None:
        return uvalue(x.uvalue)
    return x

class Update:
    def __init__(self, *args, **kwargs):
        self.sons = []
        for arg in args:
            if isinstance(getattr(arg, "sons", None), list):
                arg.sons.append(self)
        for kwarg in kwargs.values():
            if isinstance(getattr(kwarg, "sons", None), list):
                kwarg.sons.append(self)
    def update(self, *args, **kwargs):
        self.update_self(*args, **kwargs)
        for son in self.sons:
            if callable(getattr(son, "update", None)):
                son.update()
    def update_self(self, *args, **kwargs):
        pass

class Uvalue(Update):
    def __init__(self, uvalue):
        super().__init__(uvalue)
        self.uvalue = uvalue
    def update_self(self, uvalue):
        self.uvalue = uvalue

def fvalue(f, *args, **kwargs):
    return f(*(uvalue(x) for x in args), **(dict([(x, uvalue(kwargs[x])) for x in kwargs])))

class Ufunc(Update):
    def __init__(self, f, *args, **kwargs):
        super().__init__(f, *args, **kwargs)
        self.f = f
        self.uvalue = fvalue(f, *args, **kwargs)
        self.args = args
        self.kwargs = kwargs
    def update_self(self):
        self.uvalue = fvalue(self.f, *self.args, **self.kwargs)

# def add(x, y):
    # return x + y

# a = Uvalue(3)
# b = Uvalue(5)
# c = Ufunc(add, a, b)
# print(c.uvalue)
# a.update(4)
# print(c.uvalue)
# a.update(5)
# b.update(6)
# print(c.uvalue)
