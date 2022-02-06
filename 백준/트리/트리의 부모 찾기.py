from collections import deque

n = int(input())

parent = [0] * (n+1)
graph = [[] for _ in range(n+1)]

for i in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

queue = deque()
queue.append(1)

while queue:
    now = queue.popleft()
    for node in graph[now]:
        if parent[node] == 0:
            parent[node] = now
            queue.append(node)

print(*parent[2:], sep="\n")
