from collections import deque
import sys
input = sys.stdin.readline

graph = []
r, c = map(int, input().split())
for _ in range(r):
    graph.append(list(input().rstrip()))

xx = [0, 0, 1, -1]
yy = [1, -1, 0, 0]

gos_x, gos_y = -1, -1
waters = set()
bib_x, bib_y = -1, -1
for i in range(r):
    for j in range(c):
        now = graph[i][j]
        if now == "S":
            gos_x, gos_y = i, j
        elif now == "D":
            bib_x, bib_y = i, j
        elif now == "*":
            waters.add((i, j))

queue = deque()
time = 0
queue.append((gos_x, gos_y, 0))  # BFS를 위한 큐에 물과 고슴도치 이동 범위 모두 넣는다. 0, 1로 구분
for water_x, water_y in waters:
    queue.append((water_x, water_y, 1))
answer = "KAKTUS"
flag = 0
while queue:
    for _ in range(len(queue)):  # 1초 단위의 물과 고슴도치 이동 범위 큐
        now_x, now_y, isWater = queue.popleft()  # 큐 모두 소비 후 다음 턴에는 다음 초에 대한 정보 삽입
        if now_x == bib_x and now_y == bib_y:
            answer = time
            flag = 1
            break
        if isWater == 0:  # 물과 고슴 고치 경우 나눠서 조건에 해당하면 큐에 삽입
            if graph[now_x][now_y] != "*":
                graph[now_x][now_y] = "V"
                for i in range(4):
                    dx, dy = now_x+xx[i], now_y+yy[i]
                    if 0 <= dx < r and 0 <= dy < c:
                        if graph[dx][dy] == "." or graph[dx][dy] == "D":
                            queue.append((dx, dy, 0))
                            graph[dx][dy] = "V"
        else:
            for i in range(4):
                dx, dy = now_x+xx[i], now_y+yy[i]
                if 0 <= dx < r and 0 <= dy < c:
                    if graph[dx][dy] == "." or graph[dx][dy] == "V":
                        graph[dx][dy] = "*"
                        queue.append((dx, dy, 1))
    time += 1
    if flag == 1:
        break

print(answer)
