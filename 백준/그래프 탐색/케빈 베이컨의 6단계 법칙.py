import sys
input = sys.stdin.readline
INF = float('inf')
n, m = map(int, input().split())
graph = [[] for i in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

answer = []


def check(me):
    visited = [INF for i in range(n+1)]
    queue = set()
    queue.add((me, 0))
    while queue:
        now, cnt = queue.pop()
        for next in graph[now]:
            if cnt+1 < visited[next]:
                queue.add((next, cnt+1))
                visited[next] = cnt+1
    kb = 0
    for idx in range(1, n+1):
        if idx != me and visited[idx] != INF:
            kb += visited[idx]
    answer.append((kb, me))


for friend in range(1, n+1):
    check(friend)

answer.sort()
print(answer[0][1])
