import sys
EPS = 1e-7
EPS_L = 0.1 * EPS
EPS_H = 10.0 * EPS
INF = float("inf")
NINF = -INF
def sgn(x) -> int:#防止精度误差
    a = abs(x)
    if EPS_L <= a and a <= EPS_H:#在特殊范围内输出警告
        sys.stderr.write("Warning, a number neither too far nor too near to 0.\n")
    if a <= EPS:
        return 0
    if x > 0.0:
        return 1
    return -1

def eq(x, y = 0.0):
    return sgn(x - y) == 0
    
def in_range(x, l = NINF, r = INF):
    if x == NINF:
        return l == x
    if x == INF:
        return r == x
    return sgn(x-l) >= 0 and sgn(x-r) <= 0

def signed_inf(sgn:int):
    if (sgn > 0):
        return INF
    if (sgn < 0):
        return NINF
    return 0