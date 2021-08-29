import utils
import math
import sys
class Vector:
    def __init__(self, x = 0.0, y = 0.0):
        self.__x = x
        self.__y = y
    @property
    def x(self):
        return self.__x
    @x.setter
    def x(self, x):
        self.__x = x
    @property
    def y(self):
        return self.__y
    @y.setter
    def y(self, y):
        self.__y = y
    def __eq__(self, obj):
        return utils.eq(self.x, obj.x) and utils.eq(self.y, obj.y)
    def __add__(self, obj):
        return Vector(self.x+obj.x, self.y+obj.y)
    def __sub__(self, obj):
        return Vector(self.x-obj.x, self.y-obj.y)
    def __truediv__(self, obj):
        return Vector(self.x/obj, self.y/obj)
    def __mul__(self, obj):
        if isinstance(obj, Vector):
            return self.x*obj.x+self.y*obj.y
        return Vector(self.x*obj, self.y*obj)
    def __rmul__(self, obj):
        return self*obj
    def __xor__(self, obj):
        return self.x*obj.y-self.y*obj.x
    def __neg__(self):
        return Vector(-self.x, -self.y)
    def __abs__(self):
        return math.hypot(self.x, self.y)
    def __repr__(self):
        return f"({self.x}, {self.y})"
    def arg(self):
        return math.atan2(self.y, self.x)
    def update(self, obj):
        self.x = obj.x
        self.y = obj.y

Point = Vector

def point_from_k(A, B, k):
    return A * (1.0-k) + B * k

def midpoint(A, B):
    return (A + B) * 0.5

def distance(A, B):
    return abs(A - B)

def is_vector_collinear(u, v):
    return utils.eq(u^v)

def is_collinear(A, B, O = Point()):
    return is_vector_collinear(A-O, B-O)

def vector_signed_angle(u, v):
    a = math.atan2(u^v, u*v)
    if utils.eq(abs(a), math.pi):
        sys.stderr.write("Warning, calculating signed angle with angle pi.\n")
    return a

def vector_angle(u, v):
    return abs(math.atan2(u^v, u*v))

def angle(A, B, O = Point()):
    return vector_angle(A-O, B-O)
    
def signed_angle(A, B, O = Point()):
    return vector_signed_angle(A-O, B-O)

def is_vector_perpendicular(u, v):
    return utils.eq(u*v)

def is_perpendicular(A, B, O = Point()):
    return is_vector_perpendicular(A-O, B-O)

def vector_rotate(v, theta = 0.5*math.pi):
    c = math.cos(theta)
    s = math.sin(theta)
    return Vector(v.x*c-v.y*s, v.x*s+v.y*c)

def rotate(A, theta = 0.5*math.pi, O = Point()):
    return O + vector_rotate(A-O, theta)

def vector_div(u, v):
    assert v != Vector(), "Divided by 0-vector."
    assert IsVectorCollinear(u, v), "Non-collinear vectors in vector_div."
    if not utils.eq(v.x):
        return u.x/v.x
    return u.y/v.y

def get_k(C, A, B):
    return VectorDiv(C-A, B-A)

def point_to_vector_distance(A, vec):
    #give the distance between a point A and a line passing through the origin with a direction of vec.
    return abs(A^vec/abs(vec))

def point_to_vector_signed_distance(A, vec):
    #give the signed distance between a point A and a line passing through the origin with a direction of vec.
    return A^vec/abs(vec)
    
