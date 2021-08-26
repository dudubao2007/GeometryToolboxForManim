class Value:
    def __init__(self, value = 0):
        self.__value = value
    
    @property
    def value(self):
        return self.__value
    
    @value.setter
    def value(self, value):
        self.__value = value


class Func(Value):
    upd = 0
    def __init__(self, f, *args, **kwargs):
        self.__f = f
        self.__args = args
        self.__kwargs = kwargs
        self.upd = Func.upd
        self.__value = f(*args, **kwargs)
    
    @property
    def value(self):
        if Func.upd > self.upd:
            self.__value = self.__f(*self.__args, **self.__kwargs)
            self.upd = Func.upd
        return self.__value

if __name__ == "__main__":
    a = Value(3)
    F = Func(lambda x:2*x.value+1, a)
    print(F.value)
    a.value = 2
    print(F.value)