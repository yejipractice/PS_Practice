import sys
input =sys.stdin.readline
from collections import deque

n, m = map(int, input().split())

INF = float('inf')

graph = [[] for _ in range(n+1)]

distances = [[INF for i in range(n+1)] for j in range(n+1)]
for node in range(n+1):
    distances[node][node] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

flag = 0

def bfs(start, sum, visited):
    global flag
    queue = deque()
    queue.append((start, sum))
    while queue:
        now, now_cost= queue.popleft()
        for next, next_cost in graph[now]:
            if now_cost+next_cost < distances[now][next]:
                if distances[now][next] < 0:
                    flag = 1
                    return
                distances[now][next] = now_cost+next_cost
                changed = list(visited)
                changed[next] = "1"
                visited = "".join(changed)
                queue.append((next, now_cost+next_cost))
        

visited = "0"*(n+1)
bfs(1, 0, visited)

if flag == 1:
    print(-1)
else:
    for idx in range(2, n+1):
        if distances[1][idx] != INF:
            print(distances[1][idx])
        else:
            print(-1)