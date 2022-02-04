INF = float('inf')

cases = [[0, 1], [0, -1], [1, 0], [-1, 0]]

# 각 다른 가중치가 있으며 최소 비용을 찾으므로 다익스트라
for tc in range(1, int(input())+1):
    n = int(input())
    graph = []
    for _ in range(n):
        graph.append(list(map(int, input().split())))
    visited = [[INF for i in range(n)] for j in range(n)]
    visited[0][0] = 0
    queue = []
    queue.append((0, 0))
    while queue:
        now_x, now_y = queue.pop(0)
        for case in cases:
            dx, dy = now_x+case[0], now_y+case[1]
            if 0 <= dx < n and 0 <= dy < n:
                # 비교해서 더 최적화된 값이라면 방문한 것으로 하고 큐에 넣는다.
                dif = graph[dx][dy] - graph[now_x][now_y]
                if dif > 0:
                    if visited[dx][dy] > visited[now_x][now_y]+dif+1:
                        visited[dx][dy] = visited[now_x][now_y]+dif+1
                        queue.append((dx, dy))
                else:
                    if visited[dx][dy] > visited[now_x][now_y]+1:
                        visited[dx][dy] = visited[now_x][now_y]+1
                        queue.append((dx, dy))
    print("#"+str(tc), end=" ")
    print(visited[-1][-1])
