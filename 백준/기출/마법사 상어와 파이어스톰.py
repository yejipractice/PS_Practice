from collections import deque

nn, q= map(int, input().split())
n = 2**nn

board = []
for _ in range(n):
    board.append(list(map(int, input().split())))



def turn(x, y, l):
    newGraph = []
    for i in range(x, x+l):
        temp = []
        for j in range(y, y+l):
            temp.append(board[i][j])
        newGraph.append(temp)
    newGraph = list(zip(*newGraph[::-1]))
    for i in range(x, x+l):
        for j in range(y, y+l):
            a, b= i-x, j -y
            board[i][j] = newGraph[i-x][j-y]

xx = [0, 0, -1, 1]
yy = [1, -1, 0, 0]
def check():
    queue = deque()
    for x in range(n):
        for y in range(n):
            cnt = 0
            if board[x][y] < 1:
                continue
            for idx in range(4):
                dx, dy = x+xx[idx], y+yy[idx]
                if 0<=dx<n and 0<=dy<n and board[dx][dy] > 0:
                    cnt+=1
            if cnt < 3:
                queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        board[x][y] -= 1

ls = list(map(int, input().split()))
for l in ls:
    for x in range(0, n, 2**l):
        for y in range(0, n, 2**l):
            turn(x, y, 2**l)
    check()

answer = 0
for b in board:
    answer+=sum(b)

print(answer)

def bfs(x, y, num, visited):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = num
    while queue:
        now_x, now_y = queue.popleft()
        for idx in range(4):
            dx, dy = now_x+xx[idx], now_y+yy[idx]
            if 0<=dx<n and 0<=dy<n and board[dx][dy] != 0 and visited[dx][dy]==False:
                visited[dx][dy] = num
                queue.append((dx, dy))


visited = [[False for i in range(n)]for j in range(n)]
num = 1
for x in range(n):
    for y in range(n):
        if board[x][y] != 0 and visited[x][y] == False:
            bfs(x, y, num, visited)
            num+=1

max_cnt = 0
for node in range(1, num):
    cnt = 0
    for x in range(n):
        for y in range(n):
            if visited[x][y] == node:
                cnt+=1
    max_cnt = max(max_cnt, cnt)

print(max_cnt)