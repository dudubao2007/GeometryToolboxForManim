class Value:
    def __init__(self, value = 0):
        self.__value = value
    
    @property
    def value(self):
        return self.__value
    
    @value.setter
    def value(self, value):
        self.__value = value

def to_value(x):
    if hasattr(x, "value"):
        return x
    return Value(x)

class Func(Value):
    def __init__(self, f, *args, **kwargs):
        self.__f = f
        self.__args = args
        self.__kwargs = kwargs
    
    @property
    def value(self):
        return self.__f(*self.__args, **self.__kwargs)

if __name__ == "__main__":
    a = Value(3)
    F = Func(lambda x:2*x.value+1, a)
    print(F.value)
    a.value = 2
    print(F.value)