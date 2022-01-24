import sys

n = int(input())
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))
selected = [0]*n
min_sum = sys.maxsize


def dfs(array, sum):
    global min_sum
    if len(array) == n:
        first = array[0]
        last = array[-1]
        if board[last][first] != 0:
            sum += board[last][first]
            min_sum = min(min_sum, sum)
        return
    for i in range(n):
        if selected[i] == 0 and board[array[-1]][i] != 0 and sum < min_sum:
            selected[i] = 1
            dfs(array+[i], sum+board[array[-1]][i])
            selected[i] = 0


for i in range(n):
    selected[i] = 1
    dfs([i], 0)
    selected[i] = 0
print(min_sum)
