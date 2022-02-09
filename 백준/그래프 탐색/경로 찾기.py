from collections import deque
import queue
n = int(input())

graph = [[] for _ in range(n)]
answer = [[] for _ in range(n)]
board = []

for _ in range(n):
    board.append(list(map(int, input().split())))

# 각 시작점 기준으로 갈 수 있는 경로 체크
for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            graph[i].append(j)


def dfs(x):
    queue = deque()
    queue.append(x)
    while queue:
        now = queue.popleft()
        for next in graph[now]:
            if next not in answer[x]:  # visited check
                queue.append(next)
                answer[x].append(next)  # 각 시작점으로 갈 수 있는 도착점 따로 저장


# 각 시작점별로 깊이 탐색
for idx in range(n):
    dfs(idx)

result = [[0 for i in range(n)]for j in range(n)]
for idx in range(n):
    for next in answer[idx]:
        result[idx][next] = 1

for r in result:
    print(*r)

# 다익스트라로 풀 수도 있음
