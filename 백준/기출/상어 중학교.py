from collections import deque

n, m = map(int, input().split())

board = []
for _ in range(n):
    board.append((list(map(int, input().split()))))

completed = -2

def turn_left(graph):
    newGraph = []
    for t in list(reversed(list(zip(*graph)))):
        newGraph.append(list(t))
    return newGraph

def turn_down():
    for y in range(n):
        for x in range(n-1, -1, -1):
            if board[x][y] == completed:
                for nx in range(x-1, -1, -1):
                    if board[nx][y] != -1 and board[nx][y] != completed:
                        board[x][y] = board[nx][y]
                        board[nx][y] = completed
                        break
                    elif board[nx][y] == -1:
                        break

xx = [0, 0, -1, 1]
yy = [1, -1, 0, 0]

def bfs(x, y, visited):
    zeros = set()
    value = board[x][y]
    cnt = 1
    min_x, min_y = x, y
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True
    while queue:
        now_x, now_y  = queue.popleft()
        if board[now_x][now_y] != 0:
            if now_x <= min_x:
                min_x = now_x
                if now_y < min_y:
                    min_y = now_y

        for idx in range(4):
            dx, dy = now_x+xx[idx], now_y+yy[idx]
            if 0<=dx<n and 0<=dy<n:
                if (board[dx][dy] == value and visited[dx][dy] == False) or (board[dx][dy] == 0 and (dx, dy) not in zeros):
                    visited[dx][dy] = True
                    queue.append((dx, dy))
                    cnt+=1
                    if board[dx][dy] == 0:
                        zeros.add((dx, dy))
    return cnt, min_x, min_y, len(zeros)


def find_block():
    final_cnt = -1
    final_x, final_y = -1, -1
    final_zero = -1
    visited = [[False for i in range(n)]for j in range(n)]
    for x in range(n):
        for y in range(n):
            if visited[x][y] == False and board[x][y] != -1 and board[x][y] != completed and board[x][y]!=0:
                cnt, min_x, min_y, zero = bfs(x, y, visited)
                if final_cnt < cnt:
                    final_cnt = cnt
                    final_x = min_x
                    final_y = min_y
                    final_zero = zero
                elif final_cnt == cnt:
                    if final_zero < zero:
                        final_x = min_x
                        final_y = min_y
                        final_zero = zero
                    elif final_zero == zero:
                        if final_x < min_x:
                            final_x = min_x
                            final_y = min_y
                        elif final_x == min_x:
                            final_y = max(min_y, final_y)
    if final_cnt < 2:
        return -1 ,-1
    return final_x, final_y

def delete_block(x, y):
    value = board[x][y]
    board[x][y] = completed
    visited = [[False for i in range(n)] for j in range(n)]
    cnt = 1
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True
    while queue:
        now_x, now_y = queue.popleft()
        for idx in range(4):
            dx, dy = now_x + xx[idx], now_y + yy[idx]
            if 0 <= dx < n and 0 <= dy < n and (board[dx][dy] == value or board[dx][dy] == 0) and visited[dx][dy] == False:
                visited[dx][dy] = True
                queue.append((dx, dy))
                cnt += 1
                board[dx][dy] = completed
    return cnt

answer = 0
while True:
    x, y = find_block()
    if x == -1 and y == -1:
        break
    score = delete_block(x, y)
    answer += score**2
    turn_down()
    board = turn_left(board)
    turn_down()

print(answer)
