import sys
input = sys.stdin.readline

tc = int(input())
for t in range(1, tc+1):
    n = int(input())
    board = []
    for _ in range(n):
        board.append(list(map(int, input().split())))
    for x in range(n):
        for y in range(n):
            if x + y == 0 : 
                continue
            dx = x-1
            dy = y-1
            if 0<=dx<n and  0<=dy<n:
                board[x][y] += min(board[dx][y], board[x][dy])
            elif 0<=dx<n :
                board[x][y] += board[dx][y]
            elif 0<=dy<n:
                board[x][y] += board[x][dy]
    print("#"+str(t), end=" ")
    print(board[-1][-1])
                