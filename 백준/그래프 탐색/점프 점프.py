from collections import deque
import sys
input = sys.stdin.readline
INF = float('inf')

n = int(input())
lines = list(map(int, input().split()))
visited = [INF] * n


def bfs(index, cnt):
    visited[index] = cnt
    queue = deque()
    queue.append((index, cnt))
    while queue:
        idx, c = queue.popleft()
        for step in range(1, lines[idx]+1):
            next = idx+step
            if next < n and c+1 < visited[next]:
                queue.append((next, c+1))
                visited[next] = c+1


bfs(0, 0)
if visited[-1] == INF:
    print(-1)
else:
    print(visited[-1])

# bfs+dp dp를 통해서 가지치기
