from vector import *
class LineLike:
    pass
class Segment(LineLike):
    def __init__(self, start = Point(), end = Point(1, 0)):
        if (start == end):
            sys.stderr.write("Warning, the segment is too short.\n")
        self.__start = start
        self.__end = end
    @property
    def start(self):
        return self.__start
    @property
    def end(self):
        return self.__end
    @property
    def direction(self):
        return self.__end - self.__start
    def __abs__(self):
        return Distance(self.start, self.end)
    def midpoint(self):
        return midpoint(self.start, self.end)
    def point_from_k(self, k):
        return point_from_k(self.start, self.end, k)
    def __contains__(self, P):
        try:
            k = get_k(P, self.start, self.end)
        except AssertionError:
            return False
        else:
            return utils.in_range(k, 0.0, 1.0)
    def __repr__(self):
        return f"Segment({self.start}, {self.end})"

class Line(LineLike):
    def __init__(self, start = Point(), direction = Vector(1, 0)):
        if (direction == Vector()):
            sys.stderr.write("Warning, the direction vector is too short.\n")
        self.__start = start
        self.__direction = direction
    @property
    def start(self):
        return self.__start
    @property
    def end(self):
        return self.__start + self.__direction
    @property
    def direction(self):
        return self.__direction
    def __contains__(self, P):
        try:
            k = vector_div(P - self.start, self.direction)
        except AssertionError:
            return False
        else:
            return True
    def __repr__(self):
        return f"Line({self.start}, {self.direction})"
    
class HalfLine(LineLike):
    def __init__(self, start = Point(), direction = Vector(1, 0)):
        if (direction == Vector()):
            sys.stderr.write("Warning, the direction vector is too short.\n")
        self.__start = start
        self.__direction = direction
    @property
    def start(self):
        return self.__start
    @property
    def end(self):
        return self.__start + self.__direction
    @property
    def direction(self):
        return self.__direction
    def __contains__(self, P):
        try:
            k = vector_div(P - self.start, self.direction)
        except AssertionError:
            return False
        else:
            return utils.in_range(k, 0.0)
    def __repr__(self):
        return f"HalfLine({self.start}, {self.direction})"

# def GetLine(A, t, method = "AB"):
    # if (method == "AB"):
        # return Line(A, t-A)
    # if (method == "Av"):
        # return Line(A, t)
    # raise NotImplementedError

# def GetHalfLine(A, t, method = "AB"):
    # if (method == "AB"):
        # return HalfLine(A, t-A)
    # if (method == "Av"):
        # return HalfLine(A, t)
    # raise NotImplementedError

# def GetSegment(A, t, method = "AB"):
    # if (method == "AB"):
        # return Segment(A, t)
    # if (method == "Av"):
        # return Segment(A, A + t)
    # raise NotImplementedError
