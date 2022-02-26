from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

queue = deque()
for i in range(n):
    for j in range(m):
        if graph[i][j] != 0:
            queue.append((i, j, graph[i][j]))

xx = [0, 0, 1, -1]
yy = [1, -1, 0, 0]
time = 0
answer = 0

# 한 덩어리인지 체크


def check(q):
    if len(q) == 1:
        return False
    visited = [[-1 for i in range(m)]for j in range(n)]
    for qx, qy, qh in q:
        visited[qx][qy] = 0
    qq = deque()
    first_x, first_y, first_h = q[0]
    qq.append((first_x, first_y))
    while qq:
        nx, ny = qq.popleft()
        visited[nx][ny] = 1
        for i in range(4):
            dx, dy = nx+xx[i], ny+yy[i]
            if 0 <= dx < n and 0 <= dy < m and visited[dx][dy] == 0:
                qq.append((dx, dy))
                visited[dx][dy] = 1
    for v in visited:
        if 0 in v:
            return True
    return False


while queue:
    if time != 0:
        if check(queue):  # 한 덩이리인지 체크 -> 더 효율적인 방법? 있을까
            answer = time
            break
    zeros = set()
    for _ in range(len(queue)):  # 하루 단위로 빙산 녹이기
        now_x, now_y, height = queue.popleft()
        cnt = 0
        for i in range(4):
            dx, dy = now_x+xx[i], now_y+yy[i]
            if 0 <= dx < n and 0 <= dy < m and graph[dx][dy] == 0:
                cnt += 1
        if cnt < height:
            queue.append((now_x, now_y, height-cnt))
            graph[now_x][now_y] = height - cnt
        else:
            zeros.add((now_x, now_y))
    for zx, zy in zeros:  # 동시에 녹으므로 따로
        graph[zx][zy] = 0
    time += 1

print(answer)
