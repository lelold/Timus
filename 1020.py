import math


def pifagor(i1, j1, x1, y1):
    """
    returns a hypotenuse in triangle with 2 legs: x1[i1] - x1[j1]; y1[i1] - y1[j1].
    """
    return math.sqrt((x1[i1]-x1[j1])**2 + (y1[i1]-y1[j1])**2)


n, r = map(float, input().split())
n = int(n)
x = [0] * n
y = [0] * n
for i in range(n):
    x[i], y[i] = map(float, input().split())
ans = 2 * math.pi * r + pifagor(n-1, 0, x, y)
for i in range(1, n):
    ans += pifagor(i-1, i, x, y)
print("%.2f" % ans)
