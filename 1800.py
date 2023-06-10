l, h, w = map(int, input().split())
t = (2 * (h - l / 2) / 981) ** 0.5
n = t * w / 60
if l / 2 >= h:
    print('butter')
else:
    if n - int(n) < 0.25 or n - int(n) > 0.75:
        print('butter')
    else:
        print('bread')
