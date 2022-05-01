n = int(input())

graph = [[0] * 101 for _ in range(101)]
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

for i in range(n):

    y, x, d, g = map(int, input().split(' '))  # 좌표, 시작 방향, 세대
    graph[x][y] = 1

    # 커브 리스트 만들기
    curve = [d]
    for j in range(g):  # 세대 만큼 반복
        for k in range(len(curve) - 1, -1, -1):  # 모든 커브에 대해서 거꾸로 진행
            curve.append((curve[k] + 1) % 4)  # 반시계 방향으로

    # 드래곤 커브 만들기
    for j in range(len(curve)):
        x += dx[curve[j]]
        y += dy[curve[j]]
        if x < 0 or x >= 101 or y < 0 or y >= 101:
            continue

        graph[x][y] = 1

answer = 0
for i in range(100):
    for j in range(100):
        if graph[i][j] == 1 and graph[i + 1][j] == 1 and graph[i][j + 1] == 1 and graph[i + 1][j + 1] == 1:
            answer += 1

print(answer)


# 규칙 찾기가 중요
