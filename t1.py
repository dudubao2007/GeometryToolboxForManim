from manim import *
import toolbox as tb
from value import *
from intersections import Point, Segment, line_intersection, get_circumcenter, get_circle_from_center_point

DFP = tb.DotFromPoint
LFS = tb.LineFromSegment
CFC = tb.CircleFromCircle

class Test(Scene):
    def construct(self):
        A = Point(-2, 0)
        B = Point(2, 0)
        C = Point(-2, 2)
        O = tb.FuncPoint(get_circumcenter, A, B, C)
        Circ = tb.FuncCircle(get_circle_from_center_point, O, A)
        group = tb.UpdGroup(CFC(Circ), DFP(A), DFP(B), DFP(C), LFS(Segment(A, B)), LFS(Segment(A, C)), LFS(Segment(B, C)), DFP(O))
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
        group = tb.UpdGroup(A, B, C, Segment(A, B), Segment(A, C), Segment(B, C), Segment(A, F), Segment(A, E), Segment(C, E), Segment(C, D), Segment(B, D), Segment(B, F), Segment(E, F), Segment(D, F), Segment(D, E), D, E, F)
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
        