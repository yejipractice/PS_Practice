from collections import deque

cases = [[0, 1], [0, -1], [1, 0], [-1, 0]]

n = int(input())
graph = []
max_num = -1
for _ in range(n):
    line = list(map(int, input().split()))
    max_num = max(max_num, max(line))
    graph.append(line)


def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    while queue:
        now_x, now_y = queue.popleft()
        for case in cases:
            dx, dy = now_x+case[0], now_y+case[1]
            if 0 <= dx < n and 0 <= dy < n and board[dx][dy] == 0:
                board[dx][dy] = 1
                queue.append((dx, dy))


ans = 0
for h in range(1, max_num+1):  # 비의 높이 가능한 범위
    board = [[0 for i in range(n)]for j in range(n)]
    for i in range(n):
        for j in range(n):
            if graph[i][j] <= h:  # 빠진 지역
                board[i][j] = 1
    cnt = 0
    for i in range(n):
        for j in range(n):
            if board[i][j] == 0:
                bfs(i, j)
                cnt += 1
    ans = max(ans, cnt)

if max_num == 1:  # 모두 1일 경우 한 덩어리
    ans = 1

print(ans)
