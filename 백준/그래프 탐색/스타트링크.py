from collections import deque
import sys
input = sys.stdin.readline

INF = float('inf')

f, s, g, u, d = map(int, input().split())
visited = [False for i in range(f+1)]

answer = INF


def bfs(start):
    global answer
    queue = deque()
    visited[start] = True
    queue.append((start, 0))
    while queue:
        now, cnt = queue.popleft()
        if now == g:
            answer = min(answer, cnt)
        up, down = now+u, now-d
        if 1 <= up <= f and visited[up] == False:
            visited[up] = True
            queue.append((up, cnt+1))
        if 1 <= down <= f and visited[down] == False:
            visited[down] = True
            queue.append((down, cnt+1))


bfs(s)
print("use the stairs" if answer == INF else answer)
