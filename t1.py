from manim import *
from toolbox import *
from value import *
from formanim import *
from vector import Point
from line import Segment

DFP = DotFromPoint
LFS = LineFromSegment
CFC = CircleFromCircle

class Test(Scene):
    def construct(self):
        A = Point(-2, 0)
        B = Point(2, 0)
        C = Point(-2, 2)
        O = FuncPoint(get_circumcenter, A, B, C)
        Circ = FuncCircle(get_circle_from_center_point, O, A)
        group = UpdGroup(CFC(Circ), DFP(A), DFP(B), DFP(C), LFS(Segment(A, B)), LFS(Segment(A, C)), LFS(Segment(B, C)), DFP(O))
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

def trisector(A, B, O):#angle AOB's trisector nearer to A, a straight line
    t = signed_angle(A, B, O)
    D = rotate(A, t/3.0, O)
    return Segment(O, D)

class Trisector(FuncSegment):
    def __init__(self, A, B, O):
        super().__init__(trisector, A, B, O)

LI = lambda a, b:FuncPoint(line_intersection, a, b)

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
        group = UpdGroup(A, B, C, Segment(A, B), Segment(A, C), Segment(B, C), Segment(A, F), Segment(A, E), Segment(C, E), Segment(C, D), Segment(B, D), Segment(B, F), Segment(E, F), Segment(D, F), Segment(D, E), D, E, F)
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
        