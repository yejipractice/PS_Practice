from collections import defaultdict

n = int(input())
student = defaultdict(list)

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

board = [[0 for _ in range(n)] for __ in range(n)]


for _ in range(n*n):
    temp = list(map(int, input().split()))
    student[temp[0]] = temp[1:]

    max_x = 0
    max_y = 0
    max_like = -1
    max_empty = -1
    for i in range(n):
        for j in range(n):
            if board[i][j] == 0:
                likecnt = 0
                emptycnt = 0
                for k in range(4):
                    nx, ny = i+dx[k], j+dy[k]
                    if 0<=nx<n and 0<=ny<n:
                        if board[nx][ny] in temp:
                            likecnt+=1
                        if board[nx][ny] == 0:
                            emptycnt+=1

                if max_like < likecnt or (max_like == likecnt and max_empty < emptycnt):
                    max_x, max_y = i, j
                    max_like = likecnt
                    max_empty = emptycnt

    board[max_x][max_y] = temp[0]

answer = 0
for i in range(n):
    for j in range(n):
        cnt = 0
        for idx in range(4):
            nx, ny = i+dx[idx], j+dy[idx]
            if 0<=nx<n and 0<=ny<n:
                if board[nx][ny] in student[board[i][j]]:
                    cnt+=1
        if cnt!=0:
            answer+=10**(cnt-1)

print(answer)

