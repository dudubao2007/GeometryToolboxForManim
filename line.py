from vector import *
class Segment:
    def __init__(self, A = Point(), B = Point(1, 0)):
        if (A == B):
            sys.stderr.write("Warning, the segment is too short.\n")
        self.A = A.copy()
        self.B = B.copy()
    def __abs__(self):
        return Distance(self.A, self.B)
    def MidPoint(self):
        return MidPoint(self.A, self.B)
    def PointFromK(self, k):
        return PointFromK(self.A, self.B, k)
    def __contains__(self, P):
        try:
            k = GetK(P, self.A, self.B)
        except AssertionError:
            return False
        else:
            return utils.in_range(k, 0.0, 1.0)
    def copy(self):
        return Segment(self.A.copy(), self.B.copy())
    def direction(self):
        return self.B - self.A
    def reverse(self):
        return Segment(self.B, self.A)
    def line(self):
        return Line(self.A, self.B - self.A)
    def halfLine(self, rev = False):
        if rev:
            return HalfLine(self.B, self.A - self.B)
        return HalfLine(self.A, self.B - self.A)
    def Rotate(self, theta = 0.5*math.pi, O = Point()):
        return Segment(Rotate(self.A, theta, O), Rotate(self.B, theta, O))
    def update(self, obj):
        self.A = obj.A.copy()
        self.B = obj.B.copy()

class Line:
    def __init__(self, A = Point(), v = Vector(1, 0)):
        if (v == Vector()):
            sys.stderr.write("Warning, the direction vector is too short.\n")
        self.A = A.copy()
        self.v = v.copy()
        self.B = A + v
    def direction(self):
        return self.v
    def __contains__(self, P):
        try:
            k = VectorDiv(P - self.A, self.v)
        except AssertionError:
            return False
        else:
            return True
    def segment(self, a = 0.0, b = 1.0):
        return Segment(self.A + self.v * a, self.A + self.v * b)
    def halfLine(self, a = 0.0, sgn = 1):
        return HalfLine(self.A + self.v * a, self.v * sgn)
    def Rotate(self, theta = 0.5*math.pi, O = Point()):
        return Segment(Rotate(self.A, theta, O), VectorRotate(self.A.v, theta))
    def __repr__(self):
        return f"({self.A}, {self.v})"
    
class HalfLine:
    def __init__(self, A = Point(), v = Vector(1, 0)):
        if (v == Vector()):
            sys.stderr.write("Warning, the direction vector is too short.\n")
        self.A = A.copy()
        self.v = v.copy()
    def direction(self):
        return self.v
    def __contains__(self, P):
        try:
            k = VectorDiv(P - self.A, self.v)
        except AssertionError:
            return False
        else:
            return utils.in_range(k, 0.0)
    def segment(self, a = 0.0, b = 1.0):
        return Segment(self.A + self.v * a, self.A + self.v * b)
    def line(self):
        return Line(self.A, self.v)
    def Rotate(self, theta = 0.5*math.pi, O = Point()):
        return Segment(Rotate(self.A, theta, O), VectorRotate(self.A.v, theta))

def toLine(l):
    return Line(l.A, l.direction())

def IsVertical(a, b):
    return IsPerpendicular(a.direction(), b.direction())

def IsParallel(a, b):
    return IsCollinear(a.direction(), b.direction())

def LineIntersection(a, b):
    assert not IsParallel(a, b), "Parallel lines never intersect."
    return a.A - a.v * (((a.A-b.A)^(b.v)) / (a.v^b.v))

def LineLikeIntersection(a, b):
    return LineIntersection(toLine(a), toLine(b))

def ParallelLine(P, l):
    return Line(P, l.direction())

def VerticalLine(P, l):
    return Line(P, Vector(-l.direction().y, l.direction().x))

def GetLine(A, t, method = "AB"):
    if (method == "AB"):
        return Line(A, t-A)
    if (method == "Av"):
        return Line(A, t)
    raise NotImplementedError

def GetHalfLine(A, t, method = "AB"):
    if (method == "AB"):
        return HalfLine(A, t-A)
    if (method == "Av"):
        return HalfLine(A, t)
    raise NotImplementedError

def GetSegment(A, t, method = "AB"):
    if (method == "AB"):
        return Segment(A, t)
    if (method == "Av"):
        return Segment(A, A + t)
    raise NotImplementedError