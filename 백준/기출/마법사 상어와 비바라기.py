n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
moves = [tuple(map(int, input().split()))for _ in range(m)]

# 8 방향
dx8 = ("empty", 0, -1, -1, -1, 0, 1, 1, 1)
dy8 = ("empty", -1, -1, 0, 1, 1, 1, 0, -1)

# 대각 4방향
dx4 = (-1, -1,  1, 1)
dy4 = (-1,  1, -1, 1)

clouds = [(n - 1, 0), (n - 1, 1), (n - 2, 0), (n - 2, 1)]  # 구름 좌표

for d, s in moves:
    moved_cloud = []
    for x, y in clouds:
        nx, ny = (x+dx8[d]*s) % n , (y+dy8[d]*s) % n
        board[nx][ny] +=1
        moved_cloud.append((nx, ny))

    for x, y in moved_cloud:
        cnt = 0
        for d in range(4):
            nx, ny = x+dx4[d], y+dy4[d]
            if nx < 0 or nx >= n or ny < 0 or ny >= n: continue
            elif board[nx][ny] > 0: cnt+=1
        board[x][y] += cnt

    new_cloud = []
    for x in range(n):
        for y in range(n):
            if (x, y) in moved_cloud or board[x][y] < 2:
                continue
            board[x][y] -=2
            new_cloud.append((x, y))
    clouds = new_cloud

result = 0
for x in range(n):
    for y in range(n):
        result += board[x][y]

print(result)

