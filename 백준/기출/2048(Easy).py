import copy
import sys
input = sys.stdin.readline

n = int(input())

board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

# 옮기려는 방향의 반대 방향부터 거꾸로 체크해줘야 한다.
# 떨어질 곳과 이전 값을 저장하는 변수 (0일 경우 체크를 잘 해줘야 한다.)


def move_up(graph):
    new_graph = [[0 for i in range(n)]for j in range(n)]
    for column in range(n):
        pre_value = -1  # 합쳐질 가능성이 있는 이전 인덱스에 있는 값
        next_idx = 0  # 떨어질 곳
        for row in range(n):
            now = graph[row][column]
            if now != pre_value:
                new_graph[next_idx][column] = now
                if now != 0:
                    pre_value = now
                    next_idx += 1
            else:
                pre_value = -1
                new_graph[next_idx-1][column] *= 2
    return new_graph


def move_left(graph):
    new_graph = [[0 for i in range(n)]for j in range(n)]
    for row in range(n):
        pre_value = -1
        next_idx = 0
        for column in range(n):
            now = graph[row][column]
            if now != pre_value:
                new_graph[row][next_idx] = now
                if now != 0:
                    pre_value = now
                    next_idx += 1
            else:
                pre_value = -1
                new_graph[row][next_idx-1] *= 2
    return new_graph


def move_down(graph):
    new_graph = [[0 for i in range(n)]for j in range(n)]
    for column in range(n):
        pre_value = -1
        next_idx = n-1
        for row in range(n-1, -1, -1):
            now = graph[row][column]
            if now != pre_value:
                new_graph[next_idx][column] = now
                if now != 0:
                    pre_value = now
                    next_idx -= 1
            else:
                pre_value = -1
                new_graph[next_idx+1][column] *= 2
    return new_graph


def move_right(graph):
    new_graph = [[0 for i in range(n)]for j in range(n)]
    for row in range(n):
        pre_value = -1
        next_idx = n-1
        for column in range(n-1, -1, -1):
            now = graph[row][column]
            if now != pre_value:
                new_graph[row][next_idx] = now
                if now != 0:
                    pre_value = now
                    next_idx -= 1
            else:
                pre_value = -1
                new_graph[row][next_idx+1] *= 2
    return new_graph


def find_max(graph):
    ans = -1
    for g in graph:
        ans = max(ans, max(g))
    return ans


answer = -1


def dfs(graph, cnt):
    global answer
    if cnt == 5:
        answer = max(answer, find_max(graph))
        return
    dfs(move_down(graph), cnt+1)
    dfs(move_up(graph), cnt+1)
    dfs(move_right(graph), cnt+1)
    dfs(move_left(graph), cnt+1)


dfs(board, 0)
print(answer)
