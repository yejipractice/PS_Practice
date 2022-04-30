import sys
input = sys.stdin.readline

n, m, y, x, k = map(int, input().split())


#   동쪽 이동   서쪽 이동  북쪽 이동  남쪽 이동
#     1 -> 3     1 -> 4    1 -> 2    1 -> 5
#     2 -> 2     2 -> 2    2 -> 6    2 -> 1
#     3 -> 6     3 -> 1    3 -> 3    3 -> 3
#     4 -> 1     4 -> 6    4 -> 4    4 -> 4
#     5 -> 5     5 -> 5    5 -> 1    5 -> 6
#     6 -> 4     6 -> 3    6 -> 5    6 -> 2

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

order = list(map(int, input().split()))


def move(n, dice):
    if n == 1:
        return [0, dice[3], dice[2], dice[6], dice[1], dice[5], dice[4]]
    elif n == 2:
        return [0, dice[4], dice[2], dice[1], dice[6], dice[5], dice[3]]
    elif n == 3:
        return [0, dice[2], dice[6], dice[3], dice[4], dice[1], dice[5]]
    elif n == 4:
        return [0, dice[5], dice[1], dice[3], dice[4], dice[6], dice[2]]


dice = [0 for i in range(7)]

dy = [0, 0, 0, -1, 1]
dx = [0, 1, -1, 0, 0]

for i in range(len(order)):
    if y + dy[order[i]] < 0 or y + dy[order[i]] >= n or x + dx[order[i]] < 0 or x + dx[order[i]] >= m:
        continue
    x, y = x+dx[order[i]], y+dy[order[i]]
    dice = move(order[i], dice)

    if graph[y][x] == 0:
        graph[y][x] = dice[6]
    else:
        dice[6] = graph[y][x]
        graph[y][x] = 0

    print(dice[1])
