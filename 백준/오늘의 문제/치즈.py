import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split()) #높이, 너비

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

xx = [0, 0, 1, -1]
yy = [1, -1, 0, 0]

def findC(graph):
    visited = [[False for i in range(m)]for j in range(n)]
    queue = deque()
    queue.append((0, 0))
    visited[0][0] = True
    cnt=0
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            dx, dy = x+xx[i], y+yy[i]
            if 0<=dx<n and 0<=dy<m and not visited[dx][dy]:
                if graph[dx][dy] == 0:
                    visited[dx][dy] = True
                    queue.append((dx, dy))
                elif graph[dx][dy] == 1:
                    graph[dx][dy] = 0
                    visited[dx][dy] = True
                    cnt+=1
    return cnt

result = []
time = 0
while True:
    time+=1
    res = findC(graph)
    if res == 0:
        break
    else:
        result.append(res)

print(time-1)
print(result[-1])