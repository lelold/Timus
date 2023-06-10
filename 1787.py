n = list(map(int, input().split()))[0]
res = 0
for i in list(map(int, input().split())):
    i += res
    res = i - n if i - n >= 0 else 0
print(res)
