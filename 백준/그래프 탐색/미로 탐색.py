from collections import deque

n, m = map(int, input().split())
board = []
for _ in range(n):
    board.append(list(map(int, input())))
INF = float('inf')
distance = [[INF for i in range(m)] for j in range(n)]

cases = [[0, 1], [0, -1], [1, 0], [-1, 0]]
queue = deque()
queue.append([0, 0])
distance[0][0] = 1
while queue:
    now_x, now_y = queue.popleft()
    for case in cases:
        dx, dy = now_x+case[0], now_y+case[1]
        if 0 <= dx < n and 0 <= dy < m and board[dx][dy] != 0 and distance[dx][dy] == INF:
            # visited도 신경써줘야 함
            distance[dx][dy] = min(distance[dx][dy], distance[now_x][now_y]+1)
            queue.append([dx, dy])
print(distance[-1][-1])
