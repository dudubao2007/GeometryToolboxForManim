from manim import *
import toolbox as tb
from value import *
from intersections import Point, Segment, get_circumcenter, get_circle_from_center_point

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
            C = Point(-2+4*alpha, 2)
            Func.upd += 1
            obj.upd()
        self.play(
            UpdateFromAlphaFunc(group, Updater),
            run_time = 3
        )
        self.wait()