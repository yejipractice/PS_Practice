from collections import deque
import sys
input = sys.stdin.readline
INF = 100000
visited = [INF for i in range(INF+1)]

n, k = map(int, input().split())

# bfs+dp


def bfs(x):
    visited[x] = 0
    queue = deque()
    queue.append((x, 0))
    while queue:
        now, time = queue.popleft()
        if 0 <= now+1 <= INF and time+1 < visited[now+1]:
            queue.append((now+1, time+1))
            visited[now+1] = time+1
        if 0 <= now-1 <= INF and time+1 < visited[now-1]:
            queue.append((now-1, time+1))
            visited[now-1] = time+1
        if 0 <= now*2 <= INF and time < visited[now*2]:
            queue.append((now*2, time))
            visited[now*2] = time


bfs(n)
print(visited[k])
