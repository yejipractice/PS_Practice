from collections import deque

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]

def exist_fish():
    for i in range(N):
        for j in range(N):
            if 0< graph[i][j] <= 6:
                return True
    return  False

if exist_fish() == False:
    print(0)
    exit(0)

def find_shark():
    for i in range(N):
        for j in range(N):
            if graph[i][j] == 9:
                return  i, j
def bfs(x, y):
    global shark_size
    visited = [[False for i in range(N)]for j in range(N)]
    fish = []
    queue = deque()
    queue.append((0, x, y))
    while queue:
        dist, x, y = queue.popleft()
        visited[x][y] = True
        for dx, dy in d:
            nx, ny = x+dx, y+dy
            if 0<=nx<N and 0<=ny<N and not visited[nx][ny]:
                visited[nx][ny] = True
                if 1<=graph[nx][ny]<=6 and graph[nx][ny] < shark_size:
                    queue.append((dist+1, nx, ny))
                    fish.append((dist+1, nx, ny))
                elif graph[nx][ny] == 0 or graph[nx][ny] == shark_size:
                    queue.append((dist+1, nx, ny))
    if fish:
        return sorted(fish)[0]
    else:
        return False

def solve(x, y):
    global answer
    global shark_size
    eat = 0
    while True:
        fish = bfs(x, y)
        if fish:
            dist, x_shark, y_shark = fish
            graph[x_shark][y_shark] = 0
            eat+=1
            answer+=dist
            if eat== shark_size:
                shark_size+=1
                eat=0
            x, y = x_shark, y_shark
        else:
            break


shark_size = 2
d = [(-1, 0), (0, -1), (0, 1), (1, 0)]
x, y = find_shark()
graph[x][y] = 0
answer = 0
solve(x, y)
print(answer)