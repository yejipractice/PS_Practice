from collections import deque

n, k = map(int, input().split())
queue = deque()
INF = 100001  # 문제에서 주어진 최대로 제한하기
visited = [0] * (INF)
queue.append(n)

while queue:
    now = queue.popleft()
    if now == k:  # bfs이기 때문에 min 계산할 필요없이
        print(visited[now])
        break
    if 0 <= now+1 < INF and visited[now+1] == 0:
        queue.append(now+1)
        visited[now+1] = visited[now]+1
    if 0 <= now-1 < INF and visited[now-1] == 0:
        queue.append(now-1)
        visited[now-1] = visited[now]+1
    if 0 <= now*2 < INF and visited[now*2] == 0:
        queue.append(now*2)
        visited[now*2] = visited[now]+1

# bfs+dp
# dp와 visited 여부를 동시에 (메모리 효율)
