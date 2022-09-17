import sys
input = sys.stdin.readline
from collections import defaultdict
import copy
from collections import deque

n, m, fuel = map(int, input().split()) 

graph = [[0 for _ in range(n+1)]]

INF = float('inf')

for _ in range(n):
    graph.append([0]+list(map(int, input().split())))

# 그래프 초기화 
for i in range(n+1):
    for idx, vl in enumerate(graph[i]):
        if vl == 1:
            graph[i][idx] = -1
        elif vl == 0:
            graph[i][idx] = INF

start_x, start_y = map(int, input().split())

guests_info = defaultdict()

for _ in range(m):
    s1, s2, d1, d2 = map(int, input().split())
    guests_info[(s1, s2)] = (d1, d2)

guests = set(guests_info.keys())

xx = [1, -1, 0, 0]
yy = [0, 0, 1, -1]


# bfs로 시작 지점에 따른 거리 구하기 
def get_distance(x, y):
    distances = copy.deepcopy(graph)
    queue = deque()
    distances[x][y] = 0
    queue.append((x, y))
    while queue:
        now_x, now_y = queue.popleft()
        next = distances[now_x][now_y]+1
        for idx in range(4):
            next_x, next_y = now_x+xx[idx], now_y+yy[idx]
            if 1<=next_x<=n and 1<=next_y<=n and distances[next_x][next_y] != -1:
                if next < distances[next_x][next_y]:
                    distances[next_x][next_y] = next
                    queue.append((next_x, next_y))
    return distances

# 불가능 유무 
flag = True

while guests:
    now_distances = get_distance(start_x, start_y)
    min_x, min_y, min_value = INF, INF, INF
    for idx in range(len(guests)):
        guest_x, guest_y = list(guests)[idx]
        if now_distances[guest_x][guest_y] < min_value:
            min_x, min_y, min_value = guest_x, guest_y, now_distances[guest_x][guest_y]
        elif now_distances[guest_x][guest_y] == min_value:
            if guest_x < min_x:
                min_x, min_y, min_value = guest_x, guest_y, now_distances[guest_x][guest_y]
            elif guest_x == min_x:
                if guest_y < min_y:
                    min_x, min_y, min_value = guest_x, guest_y, now_distances[guest_x][guest_y]
    guests.remove((min_x, min_y))
    fuel -= min_value
    if fuel < 0:
        flag = False
        break
    des_distances = get_distance(min_x, min_y)
    des_x, des_y = guests_info[(min_x, min_y)]
    fuel -= des_distances[des_x][des_y]
    if fuel < 0:
        flag = False
        break
    start_x, start_y = des_x, des_y
    fuel += des_distances[des_x][des_y]*2

if flag==True:
    print(fuel)
else:
    print(-1)