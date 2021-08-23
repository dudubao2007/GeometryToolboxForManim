from vector import *
from line import *
from circle import *
class GetLine(Line):
    def __init__(self, start, end):
        self.__start = start
        self.__end = end
    @property
    def direction():
        return self.__end - self.__start
    @property
    def end():
        return self.__end

class GetHalfLine(HalfLine):
    def __init__(self, start, end):
        self.__start = start
        self.__end = end
    @property
    def direction():
        return self.__end - self.__start
    @property
    def end():
        return self.__end
        
GetSegment = Segment

class FuncObject(Func):
    def __init__(self, f, *args, **kwargs):
        Func.__init__(f, *args, **kwargs)
    @property
    def x():
        return self.value.x
    @property
    def y():
        return self.value.y[

class PointFromK(Point):
    def __init__(self, start, end, k):
        self.__start = start
        self.__end = end
        self.__k = to_value(k)
    @property
    def x():
        return self.__start.x * ( - self.__start
    @property
    def y():
        return self.__end

class Midpoint(Point):
    def __init__(self, start, end):
        self.__start = start
        self.__end = end
    @property
    def x():
        return __start.x *  + __end.x