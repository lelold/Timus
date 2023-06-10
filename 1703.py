import math


a, b = map(float, input().split())
v1 = tuple(map(float, input().split()))
v2 = tuple(map(float, input().split()))
v3 = [x - y for x, y in zip((0, 0, 0), v1)]
c = [x - y for x, y in zip(v2, v1)]
d = [x + y for x, y in zip(v1, [z * ((v3[0] * c[0] + v3[1]
                                      * c[1] + v3[2] * c[2])
                                     / (c[0] * c[0] + c[1]
                                        * c[1] + c[2] * c[2]))
                                for z in c])]
e = [x - y for x, y in zip(d, (0, 0, 0))]
f = [x - y for x, y in zip((0, 0, 0), d)]
g = math.sqrt(sum(f[i] * f[i] for i in range(3)))
h = math.acos(min(max(-1.0,
                      (b ** 2 - a ** 2 - g ** 2) / (- 2 * a * g)),
                  1.0))
s = math.acos(min(max(-1.0,
                      (g ** 2 - a ** 2 - b ** 2) / (- 2 * a * b)),
                  1.0))
if g <= a + b and s >= math.pi/2 - 1e-8:
    orth = [c[1] * e[2] - c[2] * e[1],
            c[2] * e[0] - c[0] * e[2],
            c[0] * e[1] - c[1] * e[0]]
    sqrorth = math.sqrt(orth[0] * orth[0]
                        + orth[1] * orth[1]
                        + orth[2] * orth[2])
    normorth = [i / sqrorth for i in orth]
    sqrr = math.sqrt(e[0] * e[0] + e[1] * e[1] + e[2] * e[2])
    normr = [i / sqrr for i in e]
    res = [x + y for x, y in zip([z * a * math.cos(h) for z in normr],
                                 [z * a * math.sin(h) for z in normorth])]
    print("%.50lf %.50lf %.50lf %.50lf" % (res[0], res[1], res[2], s))
else:
    print('No solution.')
