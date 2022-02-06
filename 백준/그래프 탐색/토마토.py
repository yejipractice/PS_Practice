from collections import deque

n, m = map(int, input().split())
tomatos = []
visited = [[False for i in range(n)] for j in range(m)]
for _ in range(m):
    tomatos.append(list(map(int, input().split())))

cases = [[0, 1], [0, -1], [1, 0], [-1, 0]]

queue = deque()

for i in range(m):
    for j in range(n):
        if tomatos[i][j] == 1:
            t = (i, j, 0)   # 익은 토마토(x, y, day)
            queue.append(t)

result = 0

# BFS
while queue:
    now_x, now_y, now_day = queue.popleft()
    result = max(result, now_day)
    for case in cases:
        dx, dy = now_x+case[0], now_y+case[1]
        if 0 <= dx < m and 0 <= dy < n and not visited[dx][dy] and tomatos[dx][dy] == 0:
            tomatos[dx][dy] = 1
            visited[dx][dy] = True
            queue.append((dx, dy, now_day+1))

for idx in range(m):  # 익지 않은 토마토 여부 체크
    if 0 in tomatos[idx]:
        result = -1

print(result)

# visited 없이 tomato에 바로 1씩 늘려 마킹한다면 시간과 메모리 절약 가능할 듯
