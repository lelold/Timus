from math import ceil


n, m = map(int, input().split())
i, oil, time = 0, 1, 2
while m / (time - 1) + i < n:
    i += m / (time - 1)
    oil = time / 2 * m
    time += 2
res = oil + (time - 1) * (n - i)
print(ceil(res))
