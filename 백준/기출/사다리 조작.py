import copy
import sys
input = sys.stdin.readline

n, m, h = map(int, input().split())
graph = [[0 for i in range(n+1)]for j in range(h+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1


def show_now(idx, graph):
    x, y = 1, idx
    for hh in range(x, h+1):
        if graph[hh][y] == 1:
            y = y+1
        elif y-1 > 0 and graph[hh][y-1] == 1:
            y = y - 1
    return y


def show_result(graph):
    for i in range(1, n+1):
        if i != show_now(i, graph):
            return False
    return True


INF = float('inf')
answer = INF


def dfs(graph, cnt, x):  # 높이 위로 다시 올라가지 않도록 가지치기 해줘야 한다. 아니면 시간 초과
    global answer
    if cnt > 3 or answer <= cnt:
        return
    if show_result(graph) == True:
        answer = min(cnt, answer)
        return
    for i in range(x, h+1):
        for j in range(1, n):
            if graph[i][j] == 0:
                if j == 1:
                    graph[i][j] = 1
                    dfs(graph, cnt+1, i)
                    graph[i][j] = 0
                elif j-1 > 0 and graph[i][j-1] == 0:
                    graph[i][j] = 1
                    dfs(graph, cnt+1, i)
                    graph[i][j] = 0
    return


dfs(graph, 0, 1)
print(-1 if answer == INF else answer)
