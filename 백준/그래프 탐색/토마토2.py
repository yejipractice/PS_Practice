from collections import deque

m, n, h = map(int, input().split())
graph = []
for _ in range(h):
    floor = []
    for i in range(n):
        floor.append(list(map(int, input().split())))
    graph.append(floor)

max_day = 0

cases = [[0, -1, 0], [0, 1, 0], [1, 0, 0], [-1, 0, 0], [0, 0, 1], [0, 0, -1]]


def bfs(tomatoes):
    global max_day
    queue = deque()
    for tomato in tomatoes:
        hh, xx, yy, day = tomato
        queue.append((hh, xx, yy, day))
    while queue:
        now_h, now_x, now_y, now_day = queue.popleft()
        max_day = max(max_day, now_day)
        for case in cases:
            dh, dx, dy = now_h+case[2], now_x+case[0], now_y+case[1]
            if 0 <= dh < h and 0 <= dx < n and 0 <= dy < m and graph[dh][dx][dy] == 0:
                graph[dh][dx][dy] = 1
                queue.append((dh, dx, dy, now_day+1))


tomatoes = []
for hh in range(h):
    for xx in range(n):
        for yy in range(m):
            if graph[hh][xx][yy] == 1:
                tomatoes.append((hh, xx, yy, 0))

bfs(tomatoes)  # 처음부터 익어있던 토마토 먼저 선별해야 visited 체크할때 이른 순으로 방문 가능

for hh in range(h):
    for xx in range(n):
        if 0 in graph[hh][xx]:
            max_day = -1


print(max_day)
