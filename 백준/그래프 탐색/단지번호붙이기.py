n = int(input())
board = []
for _ in range(n):
    board.append(list(map(int, input())))

cases = [[1, 0], [-1, 0], [0, 1], [0, -1]]


def dfs(x, y, mark):
    board[x][y] = mark
    for case in cases:
        dx, dy = x+case[0], y+case[1]
        if 0 <= dx < n and 0 <= dy < n and board[dx][dy] == 1:
            dfs(dx, dy, mark)


res = []
mark = -1
for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            dfs(i, j, mark)
            mark -= 1

check = -1
while check != mark:
    sum = 0
    for b in board:
        sum += b.count(check)
    res.append(sum)
    check -= 1

print(len(res))
res.sort()
print(*res, sep="\n")
