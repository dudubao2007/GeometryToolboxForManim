# GeometryToolboxForManim
Geometry toolbox for manim(community)

# Install
You should first make sure that manim(community version) has installed. For those who has build up a "manim environment, run  
```
pip install manim
```

# Usage
This tool is used to add geometric operation into manim.  
Maybe this will still work for shader version, or may not. We're happy to see similar tools for manimgl.

# Description
## Point and Vector
First things first, there are two fundimental things in this tool: `Point` and `Vector`.  
**Remember! `Point` and `Vector` are the same thing.**

We can use them by calling `Point(x,y)` and `Vector(x,y)`.  
If you want to get the x or y coordinates of `Point`s ot `Vector`s, do this:  
```
c = Point(2, 1)
x = c.x # x coord
y = c.y # y ccord
```  
```
c = Vector(2, 1)
x = c.x # x coord
y = c.y # y ccord
```  
We've also define the addtion, subtraction, and other operations on `Vector`s or `Point`s, see the demo code below.  
```
>>> Point(2, 3) + Point(1, 2)
Point(3, 5)
>>> Vector(1, 2) - Vecotr(2, 4)
Vector(1, 2)
>>> Vector(2, 3) * 2
Vector(4, 6)
>>> Vector(2, 3) / 2
Vector(1, 1.5)
>>> Point(3, 2) * Point(1, 2) # dot product
7
>>> Point(3, 2) ^ Point(1, 2) # cross product
4
>>> abs(Vector(3, 4)) # the magnitude
5
```

## Line
Lines is discribe by a point on the line and a direction.

## Circle
Circles is discribe by its center and radius.

# Examples
```
from manim import *
import toolbox as tb
from value import *
from intersections import Point, Segment, line_intersection, get_circumcenter, get_circle_from_center_point

class Test(Scene):
    def construct(self):
        A = Point(-2, 0)
        B = Point(2, 0)
        C = Point(-2, 2)
        O = tb.FuncPoint(get_circumcenter, A, B, C)
        Circ = tb.FuncCircle(get_circle_from_center_point, O, A)
        group = tb.UpdGroup(
            CFC(Circ), 
            DFP(A), DFP(B), DFP(C), 
            LFS(Segment(A, B)), LFS(Segment(A, C)), LFS(Segment(B, C)), 
            DFP(O)
        )
        self.add(group)
        def Updater(obj, alpha):
            C.x = -2+4*alpha
            Func.upd += 1
            obj.upd()
        self.play(
            UpdateFromAlphaFunc(group, Updater),
            run_time = 2
        )
        self.wait()
```

https://user-images.githubusercontent.com/86904416/131252494-fee4515d-c0a2-4b44-a3dd-c5e5db60e9b0.mp4

```
from manim import *
import toolbox as tb
from value import *
from intersections import Point, Segment, line_intersection, get_circumcenter, get_circle_from_center_point

DFP = tb.DotFromPoint
LFS = tb.LineFromSegment
CFC = tb.CircleFromCircle

def trisector(A, B, O):#angle AOB's trisector nearer to A, a straight line
    t = tb.signed_angle(A, B, O)
    D = tb.rotate(A, t/3.0, O)
    return Segment(O, D)

class Trisector(tb.FuncSegment):
    def __init__(self, A, B, O):
        super().__init__(trisector, A, B, O)

LI = lambda a, b:tb.FuncPoint(line_intersection, a, b)

class Morley(Scene):
    def construct(self):
        A = Point(-2, -1)
        B = Point(2, -1)
        C = Point(-2, 2)
        C_move = Segment(Point(-2, 2), Point(2, 2))
        t1 = Trisector(B, C, A)
        t2 = Trisector(C, B, A)
        t3 = Trisector(A, B, C)
        t4 = Trisector(B, A, C)
        t5 = Trisector(C, A, B)
        t6 = Trisector(A, C, B)
        D = LI(t4, t5)
        E = LI(t2, t3)
        F = LI(t1, t6)
        group = tb.UpdGroup(
            A, B, C, 
            Segment(A, B), Segment(A, C), Segment(B, C), 
            Segment(A, F), Segment(A, E), Segment(C, E), 
            Segment(C, D), Segment(B, D), Segment(B, F), 
            Segment(E, F), Segment(D, F), Segment(D, E), 
            D, E, F
        )
        group.submobjects[15].set_color(YELLOW)
        group.submobjects[16].set_color(YELLOW)
        group.submobjects[17].set_color(YELLOW)
        group.submobjects[12].set_color(RED)
        group.submobjects[13].set_color(RED)
        group.submobjects[14].set_color(RED)
        def Updater(obj, alpha):
            C.x = -2+4*alpha
            Func.upd += 1
            obj.upd()
        self.play(
            UpdateFromAlphaFunc(group, Updater),
            run_time = 3
        )
        self.wait()
```

https://user-images.githubusercontent.com/86904416/131252488-6d6107d5-9936-47f9-b07f-b45ba26ba428.mp4

# Contributing
Feel free to open an issue or pull a request, and add new operations to our project.  
Here are some operation you can contribute:

- Operations about tangent circles
- Fundimental geometry operation (bisect an angle, or reflect about a line/circle/point)
- Some calculus stuff
- ~Help this shit~
