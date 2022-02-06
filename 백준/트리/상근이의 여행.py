from collections import deque

t = int(input())


def dfs(idx, cnt):
    visited[idx] = 1
    for node in graph[idx]:
        if visited[node] == 0:
            cnt = dfs(node, cnt+1)
    return cnt


for _ in range(t):
    n, m = map(int, input().split())
    visited = [0] * (n+1)
    graph = [[] for i in range(n+1)]
    for mm in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    ans = dfs(1, 0)
    print(ans)
