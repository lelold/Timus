l, t, va, vb = map(int, input().split())
stop_al, stop_bob = 0, 0
n = int(input())
for i in range(n):
    typ, t1, d = map(int, input().split())
    if typ == 1:
        stop_al += d
    else:
        stop_bob += d
print((va * (t - stop_al) + vb * (t - stop_bob)) // l)
