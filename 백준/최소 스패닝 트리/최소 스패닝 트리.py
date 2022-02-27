import sys
input = sys.stdin.readline

v, e = map(int, input().split())

parent = [i for i in range(v+1)]
edges = []
for _ in range(e):
    a, b, value = map(int, input().split())
    edges.append((value, a, b))


def find_set(x):
    if x == parent[x]:
        return x
    parent[x] = find_set(parent[x])
    return parent[x]


def union_set(x, y):
    a = find_set(x)
    b = find_set(y)
    if b < a:
        parent[a] = b
    else:
        parent[b] = a

# 경로 압축을 해줘야 정답


edges.sort()
cnt = 0
for ee, aa, bb in edges:
    if find_set(aa) != find_set(bb):
        cnt += ee
        union_set(aa, bb)

print(cnt)
