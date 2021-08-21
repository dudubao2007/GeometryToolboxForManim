import utils
import math
import sys
class Vector:
    def __init__(self, x = 0.0, y = 0.0):
        self.x = float(x)
        self.y = float(y)
    def __eq__(self, obj):
        return utils.eq(self.x, obj.x) and utils.eq(self.y, obj.y)
    def copy(self):
        return Vector(self.x, self.y)
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

def PointFromK(A, B, k):
    return A * (1.0-k) + B * k

def MidPoint(A, B):
    return (A + B) * 0.5

def Distance(A, B):
    return abs(A - B)

def IsVectorCollinear(u, v):
    return utils.eq(u^v)

def IsCollinear(A, B, O = Point()):
    return IsVectorCollinear(A-O, B-O)

def VectorSignedAngle(u, v):
    a = math.atan2(u^v, u*v)
    if utils.eq(abs(a), math.pi):
        sys.stderr.write("Warning, calculating signed angle with angle pi.\n")
    return a

def VectorAngle(u, v):
    return abs(math.atan2(u^v, u*v))

def Angle(A, B, O = Point()):
    return VectorAngle(A-O, B-O)
    
def SignedAngle(A, B, O = Point()):
    return VectorSignedAngle(A-O, B-O)

def IsVectorPerpendicular(u, v):
    return utils.eq(u*v)

def IsPerpendicular(A, B, O = Point()):
    return IsVectorVertical(A-O, B-O)

def VectorRotate(v, theta = 0.5*math.pi):
    c = math.cos(theta)
    s = math.sin(theta)
    return Vector(v.x*c-v.y*s, v.x*s+v.y*c)

def Rotate(A, theta = 0.5*math.pi, O = Point()):
    return O + VectorRotate(A-O, theta)

def VectorDiv(u, v):
    assert v != Vector(), "Divided by 0-vector."
    assert IsVectorCollinear(u, v), "Non-collinear vectors in VectorDiv."
    if not utils.eq(v.x):
        return u.x/v.x
    return u.y/v.y

def GetK(C, A, B):
    return VectorDiv(C-A, B-A)
    