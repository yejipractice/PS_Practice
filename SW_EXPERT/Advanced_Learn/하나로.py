from itertools import combinations


def get_distance(ax, ay, bx, by):
    return ((ax-bx)**2+(ay-by)**2)


def Make_Set(p, v):
    p[v] = v


def Find_Set(p, v):
    if p[v] != v:
        return Find_Set(p, p[v])
    return p[v]


def union_set(p, n1, n2):
    p[Find_Set(p, n1)] = Find_Set(p, n2)


# 최소 비용을 기준으로 최단 경로 -> 크루스칼 알고리즘 사용
for tc in range(1, int(input())+1):
    n = int(input())
    board = []
    xs = list(map(int, input().split()))
    ys = list(map(int, input().split()))
    e = float(input())
    parent = [0] * n
    for i in range(n):
        board.append([i, xs[i], ys[i]])
        Make_Set(parent, i)
    sortedList = []

    for i, j in combinations(range(n), 2):
        sortedList.append(
            (get_distance(board[i][1], board[i][2], board[j][1], board[j][2]), i, j))

    sortedList.sort()
    cost = 0
    result = 0
    while result < n-1:
        w, start, end = sortedList.pop(0)
        if Find_Set(parent, start) != Find_Set(parent, end):
            union_set(parent, start, end)
            result += 1
            cost += w*e  # round하고 합쳐서 오답 -> 모두 다 더하고 round
    print("#"+str(tc), end=" ")
    print(round(cost))
