from collections import deque
import sys
input = sys.stdin.readline

n = int(input())

INF = 10000


def bfs(x, y):
    visited = [INF for i in range(INF+1)]
    queue = deque()
    queue.append((x, ""))
    visited[int(x)] = 0
    while queue:
        now, ops = queue.popleft()
        if int(now) == int(y):
            return ops
        if int(now)*2 > 9999:
            next1 = int(now)*2 % 10000
        else:
            next1 = int(now)*2
        if len(ops)+1 < visited[next1]:
            queue.append((str(next1), ops+"D"))
            visited[next1] = len(ops)+1
        if int(now) == 0:
            next2 = 9999
        else:
            next2 = int(now)-1
        if len(ops)+1 < visited[next2]:
            queue.append((str(next2), ops+"S"))
            visited[next2] = len(ops)+1
        now = now.zfill(4)  # zfill이 더 빠르다.
        # additional = []
        # for i in range(4-len(now)):
        #     additional.append("0")
        # additional = "".join(additional)
        # now = additional+now
        next3 = now[1:]+now[0]
        if len(ops)+1 < visited[int(next3)]:
            queue.append((next3, ops+"L"))
            visited[int(next3)] = len(ops)+1
        next4 = now[-1]+now[:3]
        if len(ops)+1 < visited[int(next4)]:
            queue.append((next4, ops+"R"))
            visited[int(next4)] = len(ops)+1


for _ in range(n):
    a, b = input().split()
    print(bfs(a, b))
