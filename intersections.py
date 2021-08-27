from vector import*
from line import*
from circle import*
from utils import*

def line_intersection(a, b):
    if is_parallel(a, b):
        print("Parallel lines, return None.")
        return None
    else:
        return a.start - a.direction * (((a.start-b.start) ^ (b.direction)) / (a.direction ^ b.direction))


def line_circle_intersection(line, circle):
    O = circle.center
    r = circle.radius
    A = line.start
    d = line.direction
    v = O - A
    # decide whether the intersection exists
    if sgn(point_to_vector_distance(v, d) - r) > 0:
        print("No intersections, return None.")
        return None
    else:
        delta = (2*v*d)**2-4*d*d*(v*v-r*r)
        if sgn(delta) == 0:
            print("Tangent, return one point.")
            return (v*d) / (2*d*d) * d+A
        else:
            p1 = (2*v*d+np.sqrt(delta)) / (2*d*d)
            p2 = (2*v*d-np.sqrt(delta)) / (2*d*d)
            return [p1*d+A, p2*d+A]


def get_tangent_point(line,circle):
    O = circle.center
    r = circle.radius
    A = line.start
    d = line.direction
    v = O - A
    if sgn(point_to_vector_distance(v, d)-r) == 0:
        return (v*d) / (2*d*d) *d
    else:
        print("Not a tangent line, return None.")
        return None

def get_line_from_equation(A, B, C):
    # get line from the equation Ax + By + C = 0
    if eq(A) and eq(B):
        print("Not A line!")
        return None
    else:
        x = -A*C/(A**2+B**2)
        y = -B*C/(A**2+B**2)
        d = Vector(-B, A)
        return Line(Point(x,y),d)

def get_radical_axis(circle1, circle2):
    x1 = circle1.center.x
    y1 = circle1.center.y
    x2 = circle2.center.x
    y2 = circle2.center.y
    r1 = circle1.radius
    r2 = circle2.radius
    f1 = x1**2+y1**2-r1**2
    f2 = x2**2+y2**2-r2**2
    A = 2*(x2-x1)
    B = 2*(y2-y1)
    C = f1-f2
    return get_line_from_equation(A,B,C)



def circle_intersection(circle1, circle2):
    radical = get_radical_axis(circle1, circle2)
    return line_circle_intersection(radical,circle1)

