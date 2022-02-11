
r, c = map(int, input().split())

graph = []
for _ in range(r):
    graph.append(list(map(str, input())))

# cases = [[0, 1], [0, -1], [1, 0], [-1, 0]] => 시간 초과, 언팩킹에 시간이 들었나보다
xx = [1, -1, 0, 0]
yy = [0, 0, 1, -1]


def bfs():
    result = 1
    queue = set([(0, 0, graph[0][0])])  # 시간 초과를 방지하기 위해 set 사용 (중복 방지)
    while queue:
        now_x, now_y, visited = queue.pop()
        for i in range(4):
            dx, dy = now_x+xx[i], now_y+yy[i]
            if 0 <= dx < r and 0 <= dy < c and graph[dx][dy] not in visited:
                newOne = visited+graph[dx][dy]
                queue.add((dx, dy, newOne))
                result = max(result, len(newOne))
    return result


print(bfs())
