import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())  # 칸 길이 수, 나무 수, 년 수

a = []
for _ in range(n):
    a.append(list(map(int, input().split())))

trees = [[[] for i in range(n)]for j in range(n)]
foods = [[5 for i in range(n)]for j in range(n)]

for _ in range(m):
    x, y, z = map(int, input().split())
    trees[x-1][y-1].append(z)

xx = [-1, -1, -1, 0, 0, 1, 1, 1]
yy = [-1, 0, 1, -1, 1, -1, 0, 1]

# 봄 여름 따로 나누지 않고 (죽은 애들 큐에 따로 담지 않고) 해야 시간 초과 나지 않음
for _ in range(k):
    # 봄 여름
    for i in range(n):
        for j in range(n):
            d = 0
            tmp = []
            if len(trees[i][j]) != 0:
                trees[i][j].sort()
                while trees[i][j]:
                    now_tree = trees[i][j].pop(0)
                    if now_tree <= foods[i][j]:
                        foods[i][j] -= now_tree
                        now_tree += 1
                        tmp.append(now_tree)
                    else:
                        d += now_tree//2
                foods[i][j] += d
                trees[i][j] = tmp
    # 가을
    for i in range(n):
        for j in range(n):
            if len(trees[i][j]) != 0:
                for tree in trees[i][j]:
                    if tree % 5 == 0:
                        for idx in range(len(xx)):
                            dx, dy = i+xx[idx], j+yy[idx]
                            if 0 <= dx < n and 0 <= dy < n:
                                trees[dx][dy].append(1)
    # 겨울
    for i in range(n):
        for j in range(n):
            foods[i][j] += a[i][j]


answer = 0
for i in range(n):
    for j in range(n):
        answer += len(trees[i][j])

print(answer)
