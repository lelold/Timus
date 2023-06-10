def dfs(st, val, number):
    """
    fills list cnt using dfs algorithm
    """
    global cnt
    if val > 50:
        return
    cnt[val] = 1 if number % 2 else -1
    for i in range(st, len(prime)):
        if prime[i] * val > 50:
            break
        dfs(i + 1, val * prime[i], number + 1)


maxn = 10001
prime = [1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
c = [[0 for i in range(55)] for j in range(55)]
cnt = [0 for ind1 in range(55)]
dfs(1, 1, 0)
num = [0 for ind2 in range(55)]
res = 0
k, s = map(int, input().split())
for i in range(1, 26):
    for j in range(i + 1):
        if j == 0 or j == i:
            c[i][j] = 1
        elif j == 1:
            c[i][j] = i
        else:
            c[i][j] = c[i - 1][j - 1] + c[i - 1][j]
for d in range(2, s + 1):
    num[d] = s // d
    if num[d] < k:
        break
    if cnt[d]:
        res += cnt[d] * c[num[d]][k]
if res >= 10000:
    print("10000")
else:
    print(res)
