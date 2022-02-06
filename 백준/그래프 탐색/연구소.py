from itertools import combinations
from collections import deque
import copy

n, m = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

cases = [[0, 1], [0, -1], [1, 0], [-1, 0]]


def count_zero(graph):
    safe = 0
    for line in graph:
        count = line.count(0)
        safe += count
    return safe


# 3개의 벽 그룹 후보들
rounded = []

# 바이러스 주변만 골랐다가 오답 -> 벽도 아니고 바이러스도 아닌 곳들 모두 후보로 넣어야 함
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            rounded.append((i, j))
            # for case in cases:
            #     dx, dy = i+case[0], j+case[1]
            #     if 0 <= dx < n and 0 <= dy < m and graph[dx][dy] == 0 and (dx, dy) not in rounded:
            #         rounded.append((dx, dy))

# 해당 후보에 대한 전파


def spread(graph):
    queue = deque()
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 2:
                queue.append((i, j))
    while queue:
        popx, popy = queue.popleft()
        for case in cases:
            dx, dy = popx+case[0], popy+case[1]
            if 0 <= dx < n and 0 <= dy < m and graph[dx][dy] == 0:
                graph[dx][dy] = 2
                queue.append((dx, dy))
    return graph


answer = 0

# 되돌리는 것보다 copy 하는 게 낫다고 판단
for case in combinations(rounded, 3):
    newGraph = copy.deepcopy(graph)
    for cx, cy in case:
        newGraph[cx][cy] = 1
    answer = max(answer, count_zero(spread(newGraph)))


print(answer)
