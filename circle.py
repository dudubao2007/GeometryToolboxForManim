from vector import *
class Circle:
    def __init__(self, center = Point(), radius = 1.0):
        self.__center = center
        self.__radius = to_value(radius)
    @property
    def center(self):
        return self.__center
    @property
    def radius(self):
        return radius.value


