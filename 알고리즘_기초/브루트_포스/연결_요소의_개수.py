import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[]for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False]*(n+1)
count = 0


def dfs(v):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(i)


for j in range(1, n+1):
    if not visited[j]:
        dfs(j)
        count += 1

print(count)
