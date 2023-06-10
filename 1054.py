n = int(input())
a = []
source, dest, aux = 1, 2, 3
res = 0
for i in range(n):
    a.append(int(input()))
while n > 0:
    if a[n-1] == source:
        dest, aux = aux, dest
    elif a[n-1] == dest:
        res += 2 ** (n-1)
        source, aux = aux, source
    else:
        print(-1)
        exit()
    n -= 1
print(res)
