def paint(x, y, i, j, n):
    """returns a field matrix with filled cells using recursion"""
    global c
    c += 1
    n = n // 2
    if x - j < n and y - i < n:
        table[i + n - 1][j + n] = c
        table[i + n][j + n - 1] = c
        table[i + n][j + n] = c
        if n > 1:
            paint(x, y, i, j, n)
            paint(j + n, i + n - 1, i, j + n, n)
            paint(j + n, i + n, i + n, j + n, n)
            paint(j + n - 1, i + n, i + n, j, n)
    elif x - j < n <= y - i:
        table[i + n - 1][j + n - 1] = c
        table[i + n][j + n] = c
        table[i + n - 1][j + n] = c
        if n > 1:
            paint(j + n - 1, i + n - 1, i, j, n)
            paint(j + n, i + n - 1, i, j + n, n)
            paint(j + n, i + n, i + n, j + n, n)
            paint(x, y, i + n, j, n)
    elif x - j >= n and y - i >= n:
        table[i + n - 1][j + n - 1] = c
        table[i + n][j + n - 1] = c
        table[i + n - 1][j + n] = c
        if n > 1:
            paint(j + n - 1, i + n - 1, i, j, n)
            paint(j + n, i + n - 1, i, j + n, n)
            paint(x, y, i + n, j + n, n)
            paint(j + n - 1, i + n, i + n, j, n)
    else:
        table[i + n - 1][j + n - 1] = c
        table[i + n][j + n - 1] = c
        table[i + n][j + n] = c
        if n > 1:
            paint(j + n - 1, i + n - 1, i, j, n)
            paint(x, y, i, j + n, n)
            paint(j + n, i + n, i + n, j + n, n)
            paint(j + n - 1, i + n, i + n, j, n)


table = [[0 for i in range(512)] for j in range(512)]
n1 = 2 ** int(input())
y1, x1 = map(lambda x: int(x) - 1, input().split())
if (n1 ** 2 - 1) % 3 != 0:
    print(-1)
    exit()
c = 0
paint(x1, y1, 0, 0, n1)
for i in range(n1):
    for j in range(n1):
        print(table[i][j], end=" ")
    print()
