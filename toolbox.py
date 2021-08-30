import vector 
import line
import circle
import utils
import math

def point_from_k(A, B, k):
    return A * (1.0-k) + B * k

def midpoint(A, B):
    return (A + B) * 0.5

def distance(A, B):
    return abs(A - B)

def is_vector_collinear(u, v):
    return utils.eq(u^v)

def is_collinear(A, B, O = vector.Point()):
    return is_vector_collinear(A-O, B-O)

def vector_signed_angle(u, v):
    a = math.atan2(u^v, u*v)
    if utils.eq(abs(a), math.pi):
        sys.stderr.write("Warning, calculating signed angle with angle pi.\n")
    return a

def vector_angle(u, v):
    return abs(math.atan2(u^v, u*v))

def angle(A, B, O = vector.Point()):
    return vector_angle(A-O, B-O)
    
def signed_angle(A, B, O = vector.Point()):
    return vector_signed_angle(A-O, B-O)

def is_vector_perpendicular(u, v):
    return utils.eq(u*v)

def is_perpendicular(A, B, O = vector.Point()):
    return is_vector_perpendicular(A-O, B-O)

def vector_rotate(v, theta = 0.5*math.pi):
    c = math.cos(theta)
    s = math.sin(theta)
    return vector.Vector(v.x*c-v.y*s, v.x*s+v.y*c)

def rotate(A, theta = 0.5*math.pi, O = vector.Point()):
    return O + vector_rotate(A-O, theta)

def is_vertical(a, b):
    return is_perpendicular(a.direction, b.direction)

def is_parallel(a, b):
    return is_collinear(a.direction, b.direction)

def parallel_line(P, l):
    return line.Line(P, l.direction)

def vertical_line(P, l):
    return line.Line(P, vector.Vector(-l.direction.y, l.direction.x))

def vector_div(u, v):
    assert v != vector.Vector(), "Divided by 0-vector."
    assert IsVectorCollinear(u, v), "Non-collinear vectors in vector_div."
    if not utils.eq(v.x):
        return u.x/v.x
    return u.y/v.y

def get_k(C, A, B):
    return VectorDiv(C-A, B-A)

def point_to_vector_distance(A, vec):
    #give the distance between a point A and a line passing through the origin with a direction of vec.
    return abs(A^vec/abs(vec))

def point_to_vector_signed_distance(A, vec):
    #give the signed distance between a point A and a line passing through the origin with a direction of vec.
    return A^vec/abs(vec)


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
    if utils.sgn(point_to_vector_distance(v, d) - r) > 0:
        print("No intersections, return None.")
        return None
    else:
        delta = (2*v*d)**2-4*d*d*(v*v-r*r)
        if utils.sgn(delta) == 0:
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
    if utils.sgn(point_to_vector_distance(v, d)-r) == 0:
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
        d = vector.Vector(-B, A)
        return line.Line(vector.Point(x,y),d)

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

def parallel_line(P, l):
    return line.Line(P, l.direction)

def vertical_line(P, l):
    return line.Line(P, vector.Vector(-l.direction.y, l.direction.x))

def get_circle_from_diameter(A, B):
    return circle.Circle(midpoint(A, B), 0.5*distance(A, B))

def get_circle_from_center_point(O, A):
    return circle.Circle(O, distance(O, A))

def get_vector_from_solving(A1, B1, C1, A2, B2, C2):
    return vector.Vector((C1*B2-C2*B1)/(A1*B2-A2*B1), (A1*C2-A2*C1)/(A1*B2-A2*B1))

def get_circumcenter(A, B, C):
    x1 = A.x
    x2 = B.x
    x3 = C.x
    y1 = A.y
    y2 = B.y
    y3 = C.y
    A1 = 2*(x2-x1)
    B1 = 2*(y2-y1)
    C1 = x2*x2+y2*y2-x1*x1-y1*y1
    A2 = 2*(x3-x2)
    B2 = 2*(y3-y2)
    C2 = x3*x3+y3*y3-x2*x2-y2*y2
    return get_vector_from_solving(A1, B1, C1, A2, B2, C2)

def get_circle_from_points(A, B, C):
    return get_circle_from_center_point(get_circumcenter(A, B, C), A)



def reflect_vector(v, l):
    return get_vector_from_solving(l.x, l.y, v*l, l.y, -l.x, l^v)
    