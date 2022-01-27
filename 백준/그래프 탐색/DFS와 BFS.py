from collections import deque

n, m, start = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for g in graph:
    g.sort()


def dfs(now):
    visited[now] = 1
    ans1.append(now)
    for next in graph[now]:
        if visited[next] == 0:
            dfs(next)


def bfs():
    global queue
    while queue:
        now = queue.popleft()
        ans2.append(now)
        for next in graph[now]:
            if visited[next] == 0:
                queue.append(next)
                visited[next] = 1


visited = [0 for _ in range(n+1)]
ans1 = []
dfs(start)
print(*ans1)

visited = [0 for _ in range(n+1)]
ans2 = []
queue = deque()
queue.append(start)
visited[start] = 1
bfs()
print(*ans2)
