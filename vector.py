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
