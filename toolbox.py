from vector import *
from line import *
from circle import *
from value import *
import manim

def to_value(x):
    if hasattr(x, "value"):
        return x
    return Value(x)

# class GetLine(Line):
    # def __init__(self, start, end):
        # self.__start = start
        # self.__end = end
    # @property
    # def direction():
        # return self.__end - self.__start
    # @property
    # def end():
        # return self.__end

# class GetHalfLine(HalfLine):
    # def __init__(self, start, end):
        # self.__start = start
        # self.__end = end
    # @property
    # def direction():
        # return self.__end - self.__start
    # @property
    # def end():
        # return self.__end
        
# GetSegment = Segment

class FuncPoint(Func, Point):
    def __init__(self, f, *args, **kwargs):
        super().__init__(f, *args, **kwargs)
    @property
    def x(self):
        return self.value.x
    @property
    def y(self):
        return self.value.y
            
class PointFromK(FuncPoint):
    def __init__(self, start, end, k):
        super().__init__(lambda s, e, v:s*(1-v.value)+e*v.value, start, end, to_value(k))

class Midpoint(PointFromK):
    def __init__(self, start, end):
        super().__init__(start, end, 0.5)

class DotFromPoint(manim.Dot):
    def __init__(self, point, **kwargs):
        self.__point = point
        self.__kwargs = kwargs
        super().__init__(point.x*manim.RIGHT+point.y*manim.UP, **kwargs)
    def upd(self):
        self.move_to(self.__point.x*manim.RIGHT+self.__point.y*manim.UP, **self.__kwargs)

class UpdGroup(manim.VGroup):
    def __init__(self, *args):
        super().__init__(*args)

# class LineFromSegment(manim.Line):
    # def __init__(self, point, **kwargs):
        # super().__init__(point.x*manim.RIGHT+point.y*manim.UP, **kwargs)
    # def upd(self):
        # self.move_to(point.x*manim.RIGHT+point.y*manim.UP, **kwargs)
        