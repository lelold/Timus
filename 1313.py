n = int(input())
a = [[0 for i1 in range(n)] for i2 in range(n)]
i, j = 0, 0
for i1 in range(n):
    row = input().split()
    for i2 in range(n):
        a[i1][i2] = int(row[i2])
for i3 in range(n):
    i = i3
    j = 0
    while i >= 0:
        print(a[i][j], end=' ')
        i -= 1
        j += 1
for i3 in range(n + 1, 2 * n):
    i = n - 1
    j = i3 - n
    while j < n:
        print(a[i][j], end=' ')
        i -= 1
        j += 1
