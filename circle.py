from vector import *
class Circle:
    def __init__(self, center = Point(), radius = 1.0):
        self.__center = center
        self.__radius = radius
    @property
    def center(self):
        return self.__center
    @property
    def radius(self):
        return self.__radius
    def __contains__(self, P):
        return utils.eq(distance(P, self.center), self.radius)


