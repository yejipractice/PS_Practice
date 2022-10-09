import  copy

N = 4
graph = [[None] * N for _ in range(N)]

for i in range(N):
    data = list(map(int, input().split()))
    for j in range(N):
        graph[i][j] = [data[2*j], data[2*j+1]-1]

d = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)]

x_shark = y_shark = 0
answer = 0

def find_fish(graph, fish):
    for i in range(N):
        for j in range(N):
            if graph[i][j][0] == fish:
                return (i, j)

def move_fish(x_shark, y_shark, graph):
    for fish in range(1, 17):
        position = find_fish(graph, fish)
        if position:
            x_fish, y_fish = position[0], position[1]
            direction = graph[x_fish][y_fish][1]
            for _ in range(len(d)):
                nx_fish, ny_fish = x_fish+d[direction][0], y_fish+d[direction][1]
                if 0<=nx_fish<N and 0<=ny_fish<N:
                    if not (nx_fish == x_shark and ny_fish == y_shark):
                        graph[x_fish][y_fish][1] = direction
                        graph[nx_fish][ny_fish], graph[x_fish][y_fish] = graph[x_fish][y_fish], graph[nx_fish][ny_fish]
                        break
                direction = (direction+1) % len(d)

def get_movable_position(x_shark, y_shark, graph):
    direction = graph[x_shark][y_shark][1]
    position = []
    for _ in range(N-1):
        x_shark+=d[direction][0]
        y_shark+=d[direction][1]
        if 0<=x_shark< N and 0<=y_shark<N and graph[x_shark][y_shark][0] != -1:
            position.append((x_shark, y_shark))
    return  position

def dfs(x_shark, y_shark, eat, graph):
    global answer
    graph = copy.deepcopy(graph)
    eat+=graph[x_shark][y_shark][0]
    graph[x_shark][y_shark][0] = -1
    move_fish(x_shark, y_shark, graph)
    position = get_movable_position(x_shark, y_shark, graph)

    if position:
        for nx_shark, ny_shark in position:
            dfs(nx_shark, ny_shark, eat, graph)
    else:
        answer = max(answer, eat)
        return


dfs(x_shark, y_shark, 0, graph)
print(answer)