import copy
from itertools import combinations
from collections import deque
import sys
input = sys.stdin.readline

xx = [0, 0, 1, -1]
yy = [1, -1, 0, 0]

INF = float('inf')

n, m = map(int, input().split())
graph = [[INF for i in range(n)]for j in range(n)]
viruses = []
for row in range(n):
    inp = list(map(int, input().split()))
    for column in range(n):
        if inp[column] == 2:
            viruses.append((row, column))
        elif inp[column] == 1:
            graph[row][column] = -1


def bfs(graph, queue):
    while queue:
        now_x, now_y, cost = queue.popleft()
        for idx in range(4):
            dx, dy = now_x+xx[idx], now_y+yy[idx]
            if 0 <= dx < n and 0 <= dy < n and graph[dx][dy] != -1 and cost+1 < graph[dx][dy]:
                graph[dx][dy] = cost+1
                queue.append((dx, dy, cost+1))
    for vx, vy in viruses:  # 비활성화여도 빈칸만 없으면 괜찮다
        graph[vx][vy] = 0
    ans = -1
    for g in graph:
        ans = max(ans, max(g))
    return ans


answer = INF

for virus_array in combinations(viruses, m):
    tmp_graph = copy.deepcopy(graph)
    queue = deque()
    for vx, vy in virus_array:
        tmp_graph[vx][vy] = 0
        queue.append((vx, vy, 0))
    result = bfs(tmp_graph, queue)
    answer = min(answer, result)
if answer == INF:
    answer = -1
print(answer)
