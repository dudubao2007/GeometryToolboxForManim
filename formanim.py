import vector
import line
import circle
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

class FuncPoint(Func, vector.Point):
    def __init__(self, f, *args, **kwargs):
        super().__init__(f, *args, **kwargs)
    @property
    def x(self):
        return self.value.x
    @property
    def y(self):
        return self.value.y

class FuncSegment(Func, line.Segment):
    def __init__(self, f, *args, **kwargs):
        super().__init__(f, *args, **kwargs)
    @property
    def start(self):
        return self.value.start
    @property
    def end(self):
        return self.value.end
    @property
    def direction(self):
        return self.value.direction

class FuncCircle(Func, circle.Circle):
    def __init__(self, f, *args, **kwargs):
        super().__init__(f, *args, **kwargs)
    @property
    def center(self):
        return self.value.center
    @property
    def radius(self):
        return self.value.radius
            
# class PointFromK(FuncPoint):
    # def __init__(self, start, end, k):
        # super().__init__(lambda s, e, v:s*(1-v.value)+e*v.value, start, end, to_value(k))

# class Midpoint(PointFromK):
    # def __init__(self, start, end):
        # super().__init__(start, end, 0.5)

def to_pos(point):
    return point.x*manim.RIGHT+point.y*manim.UP

class DotFromPoint(manim.Dot):
    def __init__(self, point, **kwargs):
        self.point = point
        super().__init__(to_pos(point), **kwargs)
        point.dot = self
    def upd(self):
        self.move_to(to_pos(self.point))


# class LineFromSegment(manim.Line):
    # def __init__(self, segment, use_dot = True, **kwargs):
        # self.segment = segment
        # if use_dot and hasattr(self.segment.start, "dot") and hasattr(self.segment.end, "dot"):
            # super().__init__(segment.start.dot, segment.end.dot, **kwargs)
        # else:
            # super().__init__(to_pos(segment.start), to_pos(segment.end), **kwargs)
        # segment.line = self
    # def upd(self):
        # self.put_start_and_end_on(to_pos(self.segment.start), to_pos(self.segment.end))

class LineFromSegment(manim.Line):
    def __init__(self, segment, **kwargs):
        self.segment = segment
        super().__init__(to_pos(segment.start), to_pos(segment.end), **kwargs)
        segment.line = self
    def upd(self):
        self.put_start_and_end_on(to_pos(self.segment.start), to_pos(self.segment.end))

class CircleFromCircle(manim.Circle):
    def __init__(self, circle, **kwargs):
        self.circle = circle
        super().__init__(arc_center = to_pos(circle.center), radius = circle.radius, **kwargs)
        circle.circle = self
    def upd(self):
        self.move_to(to_pos(self.circle.center)).set_width(self.circle.radius*2)

def to_manim(obj):
    if isinstance(obj, manim.VMobject):
        return obj
    if isinstance(obj, vector.Point):
        return DotFromPoint(obj)
    if isinstance(obj, line.Segment):
        return LineFromSegment(obj)
    if isinstance(obj, circle.Circle):
        return CircleFromCircle(obj)
    return NotImplementedError

class UpdGroup(manim.VGroup):
    def __init__(self, *args):
        super().__init__(*[to_manim(arg) for arg in args])
    def upd(self):
        for mobject in self.submobjects:
            mobject.upd()