import copy
from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

queue = []
for i in range(n):
    for j in range(m):
        if graph[i][j] != 0 and graph[i][j] != 6:
            queue.append((i, j, graph[i][j]))

xx = [0, 0, 1, -1]
yy = [1, -1, 0, 0]


def four_one_turn(graph, x, y, time):
    board = copy.deepcopy(graph)
    next = fill_down(board, x, y)
    dfs(next, time)
    board = copy.deepcopy(graph)
    next = fill_up(board, x, y)
    dfs(next, time)
    board = copy.deepcopy(graph)
    next = fill_right(board, x, y)
    dfs(next, time)
    board = copy.deepcopy(graph)
    next = fill_left(board, x, y)
    dfs(next, time)
    return


def fill_right(board, x, y):
    for idx in range(y+1, m):
        if board[x][idx] == 6:
            break
        elif board[x][idx] == 0:
            board[x][idx] = "#"
    return board


def fill_left(board, x, y):
    for idx in range(y-1, -1, -1):
        if board[x][idx] == 6:
            break
        elif board[x][idx] == 0:
            board[x][idx] = "#"
    return board


def fill_up(board, x, y):
    for idx in range(x-1, -1, -1):
        if board[idx][y] == 6:
            break
        elif board[idx][y] == 0:
            board[idx][y] = "#"
    return board


def fill_down(board, x, y):
    for idx in range(x+1, n):
        if board[idx][y] == 6:
            break
        elif board[idx][y] == 0:
            board[idx][y] = "#"
    return board


def four_three_turn(graph, x, y, time):
    board = copy.deepcopy(graph)
    fill_up(board, x, y)
    fill_left(board, x, y)
    dfs(board, time)
    board = copy.deepcopy(graph)
    fill_up(board, x, y)
    fill_right(board, x, y)
    dfs(board, time)
    board = copy.deepcopy(graph)
    fill_down(board, x, y)
    fill_right(board, x, y)
    dfs(board, time)
    board = copy.deepcopy(graph)
    fill_down(board, x, y)
    fill_left(board, x, y)
    dfs(board, time)
    return


def four_four_turn(graph, x, y, time):
    board = copy.deepcopy(graph)
    fill_up(board, x, y)
    fill_down(board, x, y)
    fill_left(board, x, y)
    dfs(board, time)
    board = copy.deepcopy(graph)
    fill_up(board, x, y)
    fill_down(board, x, y)
    fill_right(board, x, y)
    dfs(board, time)
    board = copy.deepcopy(graph)
    fill_up(board, x, y)
    fill_left(board, x, y)
    fill_right(board, x, y)
    dfs(board, time)
    board = copy.deepcopy(graph)
    fill_down(board, x, y)
    fill_left(board, x, y)
    fill_right(board, x, y)
    dfs(board, time)
    return


def one_turn(graph, x, y, time):
    board = copy.deepcopy(graph)
    for idx in range(x+1, n):
        if board[idx][y] == 6:
            break
        elif board[idx][y] == 0:
            board[idx][y] = "#"
    for idx in range(x-1, -1, -1):
        if board[idx][y] == 6:
            break
        elif board[idx][y] == 0:
            board[idx][y] = "#"
    for idx in range(y+1, m):
        if board[x][idx] == 6:
            break
        elif board[x][idx] == 0:
            board[x][idx] = "#"
    for idx in range(y-1, -1, -1):
        if board[x][idx] == 6:
            break
        elif board[x][idx] == 0:
            board[x][idx] = "#"
    dfs(board, time)
    return


def two_turn(graph, x, y, time):
    board = copy.deepcopy(graph)
    for idx in range(x+1, n):
        if board[idx][y] == 6:
            break
        elif board[idx][y] == 0:
            board[idx][y] = "#"
    for idx in range(x-1, -1, -1):
        if board[idx][y] == 6:
            break
        elif board[idx][y] == 0:
            board[idx][y] = "#"
    dfs(board, time)
    board = copy.deepcopy(graph)
    for idx in range(y+1, m):
        if board[x][idx] == 6:
            break
        elif board[x][idx] == 0:
            board[x][idx] = "#"
    for idx in range(y-1, -1, -1):
        if board[x][idx] == 6:
            break
        elif board[x][idx] == 0:
            board[x][idx] = "#"
    dfs(board, time)


def count(board):
    cnt = 0
    for i in range(n):
        for j in range(m):
            if board[i][j] == 0:
                cnt += 1
    return cnt


answer = float('inf')


def dfs(graph, time):
    global queue
    global answer
    if time == 0:
        res = count(graph)
        answer = min(answer, res)
    else:
        x, y, type = queue[len(queue)-time]
        time -= 1
        if type == 5:
            one_turn(graph, x, y, time)
        elif type == 2:
            two_turn(graph, x, y, time)
        elif type == 1:
            four_one_turn(graph, x, y, time)
        elif type == 3:
            four_three_turn(graph, x, y, time)
        elif type == 4:
            four_four_turn(graph, x, y, time)


dfs(graph, len(queue))
print(answer)
