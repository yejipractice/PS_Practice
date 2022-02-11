from collections import deque

cases = [[-2, 1], [-1, 2], [1, 2], [2, 1],
         [2, -1], [1, -2], [-1, -2], [-2, -1]]


def bfs(x, y, time):
    queue = deque()
    queue.append((x, y, time))
    while queue:
        now_x, now_y, now = queue.popleft()
        if now_x == goal_x and now_y == goal_y:
            return now
        for case in cases:
            dx, dy = now_x+case[0], now_y+case[1]
            if 0 <= dx < n and 0 <= dy < n and graph[dx][dy] == 0:
                graph[dx][dy] = 1
                queue.append((dx, dy, now+1))


for _ in range(int(input())):
    n = int(input())
    graph = [[0 for i in range(n)]for j in range(n)]
    x, y = map(int, input().split())
    goal_x, goal_y = map(int, input().split())
    graph[x][y] = 1
    print(bfs(x, y, 0))
