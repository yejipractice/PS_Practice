import sys
input = sys.stdin.readline

n, m = map(int, input().split())
parent = [i for i in range(n+1)]
edges = []
for _ in range(m):
    a, b, w = map(int, input().split())
    edges.append((w, a, b))
edges.sort()


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


cnt = 0
total = 0

for idx in range(len(edges)):
    if cnt >= n-2:
        break
    cost, aa, bb = edges[idx]
    if find_set(aa) != find_set(bb):
        union_set(aa, bb)
        cnt += 1
        total += cost

print(total)
