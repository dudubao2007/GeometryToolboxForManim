from vector import *
from utils import *
from line import *
A = Point(1, 2)
B = Point(3, 4)
l = Segment(A, B)
print(l)
A.x = 2
print(l)