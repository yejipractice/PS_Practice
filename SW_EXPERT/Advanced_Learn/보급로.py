from collections import deque

INF = float('inf')  # INF 설정

cases = [[0, 1], [0, -1], [1, 0], [-1, 0]]

# 다익스트라 알고리즘 이용
for tc in range(1, int(input())+1):
    n = int(input())
    board = []
    distance = []
    for _ in range(n):
        board.append(list(map(int, list(input()))))
        distance.append([INF for i in range(n)])
    queue = deque()
    queue.append([0, 0])
    distance[0][0] = 0
    while queue:
        x, y = queue.popleft()
        for case in cases:
            dx, dy = x+case[0], y+case[1]
            if 0 <= dx < n and 0 <= dy < n:
                if distance[dx][dy] > distance[x][y]+board[dx][dy]:
                    distance[dx][dy] = distance[x][y]+board[dx][dy]
                    queue.append([dx, dy])
    print("#"+str(tc)+" "+str(distance[-1][-1]))
