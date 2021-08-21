from formanim import *
from line import Segment, LineIntersection, GetLine, GetSegment
from vector import Point, MidPoint
from update import *
PD = PointDot
UPD = UpdatePointDot
SL = SegmentLine
USL = UpdateSegmentLine
class Tri(Scene):
    def construct(self):
        A, a = PD(Point(-2, -2))
        B, b = PD(Point(2, -2))
        C, c = PD(Point(-2, 2))
        sa = Line(b, c)
        sb = Line(a, c)
        sc = Line(a, b)
        D, d = PD(MidPoint(B, C))
        E, e = PD(MidPoint(A, C))
        F, f = PD(MidPoint(A, B))
        sd = Line(e, f)
        se = Line(d, f)
        sf = Line(d, e)
        self.add(a, b, c, sa, sb, sc, d, e, f, sd, se, sf)
        def Updater(none):
            C = toPoint(c)
            sa.become(Line(b, c))
            sb.become(Line(a, c))
            UPD(D, d, MidPoint(B, C))
            UPD(E, e, MidPoint(A, C))
            sd.become(Line(e, f))
            se.become(Line(d, f))
            sf.become(Line(d, e))
        self.play(
            c.animate.shift(4 * RIGHT), 
            UpdateFromFunc(None, Updater),
            run_time = 2
        )
        self.wait()

def Trisector(A, B, O):#angle AOB's trisector nearer to A, a straight line
    t = vt.SignedAngle(A, B, O)
    D = vt.Rotate(A, t/3.0, O)
    return GetLine(O, D)

class Morley0(Scene):
    def construct(self):
        A, a = PD(Point(-2, -2))
        B, b = PD(Point(2, -2))
        C, c = PD(Point(-2, 2))
        SA, sa = SL(Segment(B, C))
        SB, sb = SL(Segment(A, C))
        SC, sc = SL(Segment(A, B))
        t1 = Trisector(B, C, A)
        t2 = Trisector(C, B, A)
        t3 = Trisector(A, B, C)
        t4 = Trisector(B, A, C)
        t5 = Trisector(C, A, B)
        t6 = Trisector(A, C, B)
        D, d = PD(LineIntersection(t4, t5))
        E, e = PD(LineIntersection(t2, t3))
        F, f = PD(LineIntersection(t1, t6))
        SD, sd = SL(Segment(E, F))
        SE, se = SL(Segment(D, F))
        SF, sf = SL(Segment(D, E))
        assert(utils.eq(abs(SD), abs(SE)) and utils.eq(abs(SE), abs(SF)))
        L1, l1 = SL(Segment(A, F))
        L2, l2 = SL(Segment(A, E))
        L3, l3 = SL(Segment(C, E))
        L4, l4 = SL(Segment(C, D))
        L5, l5 = SL(Segment(B, D))
        L6, l6 = SL(Segment(B, F))
        self.add(a, b, c, sa, sb, sc, l1, l2, l3, l4, l5, l6, d, e, f, sd, se, sf)
        def Updater(none):
            C = toPoint(c)
            USL(SA, sa, Segment(B, C))
            USL(SB, sb, Segment(A, C))
            USL(SC, sc, Segment(A, B))
            t1 = Trisector(B, C, A)
            t2 = Trisector(C, B, A)
            t3 = Trisector(A, B, C)
            t4 = Trisector(B, A, C)
            t5 = Trisector(C, A, B)
            t6 = Trisector(A, C, B)
            UPD(D, d, LineIntersection(t4, t5))
            UPD(E, e, LineIntersection(t2, t3))
            UPD(F, f, LineIntersection(t1, t6))
            #print(D, toPoint(d))
            USL(SD, sd, Segment(E, F))
            USL(SE, se, Segment(D, F))
            USL(SF, sf, Segment(D, E))
            assert(utils.eq(abs(SD), abs(SE)) and utils.eq(abs(SE), abs(SF)))
            USL(L1, l1, Segment(A, F))
            USL(L2, l2, Segment(A, E))
            USL(L3, l3, Segment(C, E))
            USL(L4, l4, Segment(C, D))
            USL(L5, l5, Segment(B, D))
            USL(L6, l6, Segment(B, F))
        self.play(
            c.animate.shift(4 * RIGHT), 
            UpdateFromFunc(None, Updater),
            run_time = 4
        )
        self.wait()

class Morley(Scene):
    def construct(self):
        A, a = UvalueDot(Point(-2, -2))
        B, b = UvalueDot(Point(2, -2))
        C, c = UvalueDot(Point(-2, 2))
        C_move = Segment(Point(-2, 2), Point(2, 2))
        SA, sa = UfuncLine(GetSegment, B, C)
        SB, sb = UfuncLine(GetSegment, A, C)
        SC, sc = UfuncLine(GetSegment, A, B)
        t1 = Ufunc(Trisector, B, C, A)
        t2 = Ufunc(Trisector, C, B, A)
        t3 = Ufunc(Trisector, A, B, C)
        t4 = Ufunc(Trisector, B, A, C)
        t5 = Ufunc(Trisector, C, A, B)
        t6 = Ufunc(Trisector, A, C, B)
        D, d = UfuncDot(LineIntersection, t4, t5)
        E, e = UfuncDot(LineIntersection, t2, t3)
        F, f = UfuncDot(LineIntersection, t1, t6)
        d.set_kwargs(color = YELLOW)
        e.set_kwargs(color = YELLOW)
        f.set_kwargs(color = YELLOW)
        SD, sd = UfuncLine(GetSegment, E, F)
        SE, se = UfuncLine(GetSegment, D, F)
        SF, sf = UfuncLine(GetSegment, D, E)
        sd.set_kwargs(color = RED, buff = d.uvalue.radius)
        se.set_kwargs(color = RED, buff = d.uvalue.radius)
        sf.set_kwargs(color = RED, buff = d.uvalue.radius)
        L1, l1 = UfuncLine(GetSegment, A, F)
        L2, l2 = UfuncLine(GetSegment, A, E)
        L3, l3 = UfuncLine(GetSegment, C, E)
        L4, l4 = UfuncLine(GetSegment, C, D)
        L5, l5 = UfuncLine(GetSegment, B, D)
        L6, l6 = UfuncLine(GetSegment, B, F)
        self.add(*[x.uvalue for x in [a, b, c, sa, sb, sc, l1, l2, l3, l4, l5, l6, d, e, f, sd, se, sf]])
        def Updater(none, alpha):
            C.update(C_move.PointFromK(alpha))
        self.play(UpdateFromAlphaFunc(c.uvalue, Updater, run_time = 4))
        self.wait()

def midPoint(P, Q):
    return UfuncDot(MidPoint, P, Q)
def getSegment(P, Q):
    return UfuncLine(GetSegment, P, Q)

class Sierpinski(Scene):
    def construct(self):
        def Add(*args):
            self.add(*[uvalue(x) for x in args])
        def dfs(A, B, C, depth = 3):
            if (depth <= 0):
                return 
            D, d = midPoint(B, C)
            E, e = midPoint(A, C)
            F, f = midPoint(A, B)
            SD, sd = getSegment(E, F)
            SE, se = getSegment(D, F)
            SF, sf = getSegment(D, E)
            sd.uvalue.set_stroke(width = 0.1)
            se.uvalue.set_stroke(width = 0.1)
            sf.uvalue.set_stroke(width = 0.1)
            #Add(d, e, f, sd, se, sf)
            Add(sd, se, sf)
            dfs(A, F, E, depth-1)
            dfs(F, B, D, depth-1)
            dfs(E, D, C, depth-1)
        A, a = UvalueDot(Point(-2, -2))
        B, b = UvalueDot(Point(2, -2))
        C, c = UvalueDot(Point(-0.5, 2))
        SA, sa = getSegment(B, C)
        SB, sb = getSegment(A, C)
        SC, sc = getSegment(A, B)
        Add(sa, sb, sc)
        C_move = Segment(Point(-0.5, 2), Point(0.5, 2))
        dfs(A, B, C)
        def Updater(none, alpha):
            C.update(C_move.PointFromK(rate_functions.smooth(alpha)))
        self.play(UpdateFromAlphaFunc(uvalue(sa), Updater, run_time = 1.5))
        self.wait()
            