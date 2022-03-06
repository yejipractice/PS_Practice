import sys
input = sys.stdin.readline

n = int(input())
xs = []
ys = []
zs = []
for _ in range(n):
    x, y, z = map(int, input().split())
    xs.append((x, _))
    ys.append((y, _))
    zs.append((z, _))

parent = [i for i in range(n+1)]


def find_set(x):
    if parent[x] != x:
        parent[x] = find_set(parent[x])
    return parent[x]


def union_set(x, y):
    a, b = find_set(x), find_set(y)
    if b < a:
        parent[a] = b
    else:
        parent[b] = a


edges = []

xs.sort()
ys.sort()
zs.sort()

# 간선 모두 구하기 -> 메모리 초과 -> n^2
# 각 위치별 거리 n-1개씩 구하기 3*n

for idx in range(n-1):
    edges.append((xs[idx+1][0]-xs[idx][0], xs[idx][1], xs[idx+1][1]))
    edges.append((ys[idx+1][0]-ys[idx][0], ys[idx][1], ys[idx+1][1]))
    edges.append((zs[idx+1][0]-zs[idx][0], zs[idx][1], zs[idx+1][1]))

cnt = 0
total = 0


edges.sort()
for _ in range(len(edges)):
    if cnt >= n-1:
        break
    w, aa, bb = edges[_]
    if find_set(aa) != find_set(bb):
        union_set(aa, bb)
        total += w
        cnt += 1

print(total)
