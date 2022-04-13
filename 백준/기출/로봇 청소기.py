from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
r, c, d = map(int, input().split())
board = []
for i in range(n):
    board.append(list(map(int, input().split())))


def turn_left(d):
    if d == 0:
        return 3
    else:
        return d-1


# 가야할 방향을 바로 넣어주기
# 뒤로 가야할 때는 그냥 뺴주면 됨
xx = [-1, 0, 1, 0]
yy = [0, 1, 0, -1]


while 1:
    board[r][c] = -1
    flag = True
    for i in range(4):
        d = turn_left(d)
        dx, dy = r+xx[d], c+yy[d]
        if 0 <= dx < n and 0 <= dy < m and board[dx][dy] == 0:
            r, c = dx, dy
            flag = False
            break
    if flag == True:
        back_x, back_y = r-xx[d], c-yy[d]
        if board[back_x][back_y] != 1:
            r, c = back_x, back_y
        else:
            break

answer = 0
for i in range(n):
    for j in range(m):
        if board[i][j] == -1:
            answer += 1


print(answer)
