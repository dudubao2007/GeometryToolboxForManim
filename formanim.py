import vector as vt
import line
from manim import *
import utils
from update import *
import types
def toPoint(d):
    return vt.Point(d.get_center()[0], d.get_center()[1])

def toDot(p, **kwargs):
    return Dot(np.array([p.x, p.y, 0]), **kwargs)

def PointDot(p, **kwargs):
    return p, toDot(p, **kwargs)

def DotPoint(d):
    return d, toPoint(d)

def UpdatePointDot(p, d, sp, **kwargs):
    p.update(sp)
    d.become(toDot(p, **kwargs))

def UpdateDotPoint(d, p, sd):
    d.become(sd)
    p = toPoint(d)

def toSegment(l):
    return line.Segment(Point(s.start[0], s.start[1]), Point(s.end[0], s.end[1]))

def toLine(s, **kwargs):
    return Line(np.array([s.A.x, s.A.y, 0]), np.array([s.B.x, s.B.y, 0]), **kwargs)

def SegmentLine(s, **kwargs):
    return s, toLine(s, **kwargs)

def LineSegment(l):
    return l, toSegment(l)

def UpdateSegmentLine(s, l, ss):
    s.update(ss)
    l.put_start_and_end_on(np.array([s.A.x, s.A.y, 0]), np.array([s.B.x, s.B.y, 0]))

def UpdateLineSegment(s, l, sl):
    l.become(sl)
    s = toPoint(l)


class UDot(Update):
    def __init__(self, point, **kwargs):
        super().__init__(point)
        self.point = point
        self.uvalue = toDot(uvalue(point), **kwargs)
        self.kwargs = kwargs
    def set_kwargs(self, **kwargs):
        self.uvalue.become(toDot(uvalue(self.point), **kwargs))
        self.kwargs = kwargs
    def update_self(self):
        self.uvalue.become(toDot(uvalue(self.point), **self.kwargs))

class ULine(Update):
    def __init__(self, seg, **kwargs):
        super().__init__(seg)
        self.seg = seg
        self.uvalue = toLine(uvalue(seg), **kwargs)
        self.kwargs = kwargs
    def set_kwargs(self, **kwargs):
        self.uvalue.become(toLine(uvalue(self.seg), **kwargs))
        self.kwargs = kwargs
    def update_self(self):
        self.uvalue.become(toLine(uvalue(self.seg), **self.kwargs))

class UDotLine(Update):
    def __init__(self, a, b, **kwargs):
        super().__init__(a, b)
        self.a = a
        self.b = b
        self.uvalue = Line(uvalue(a), uvalue(b), **kwargs)
        self.kwargs = kwargs
    def set_kwargs(self, **kwargs):
        self.uvalue.become(Line(uvalue(self.a), uvalue(self.b), **self.kwargs))
        self.kwargs = kwargs
    def update_self(self):
        self.uvalue.put_start_and_end_on(uvalue(self.a).get_center(), uvalue(self.b).get_center())#self.uvalue.account_for_buff(uvalue(self.a).radius)

def UvalueDot(p):
    P = Uvalue(p)
    return P, UDot(P)

def UvalueLine(l):
    l = Uvalue(l)
    return l, ULine(l)

def UDLine(A, B, a = None, b = None, **kwargs):
    if a is None:
        a = UDot(A)
    if b is None:
        b = UDot(B)
    s = Ufunc(line.GetSegment, A, B)
    l = UDotLine(a, b, **kwargs)
    return s, l

def UfuncDot(f, *args, **kwargs):
    P = Ufunc(f, *args, **kwargs)
    return P, UDot(P)

def UfuncLine(f, *args, **kwargs):
    l = Ufunc(f, *args, **kwargs)
    return l, ULine(l)