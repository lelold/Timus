def dfs(v, col, g, c):
    """
    returns True if vertex can be painted else False
    """
    if c[v] != -1 and c[v] == col:
        return True
    elif c[v] != -1 and c[v] != col:
        return False
    c[v] = col
    for i in range(len(g)):
        if g[v][i] and not dfs(i, 1 - col, g, c):
            return False
    return True


n = int(input())
graph = [[0] * n for i in range(n)]
for i in range(n):
    neighbors = list(map(int, input().split()))[:-1]
    for j in neighbors:
        graph[i][j-1] = graph[j-1][i] = 1
colors = [-1] * n
if dfs(0, 0, graph, colors):
    print(''.join(map(str, colors)))
else:
    print("-1")
