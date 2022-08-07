import queue
import sys
from turtle import distance
input = sys.stdin.readline
import heapq

n, m = map(int, input().split())
INF = float('inf')
graph = [[] for _ in range(n+1)]
distance = [INF for _ in range(n+1)]
visited = [False for _ in range(n+1)]

def dijk(start):
    queue = []
    heapq.heappush(queue, (start, 0))
    while queue:
        now, dist = heapq.heappop(queue)
        if distance[now] < dist:
            continue
        for i, c in graph[now]:
            cost = dist+c
            if cost < distance[i]:
                distance[i] = cost
                heapq.heappush(queue, (i, cost))

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
    
dijk(1)
print(distance[-1])