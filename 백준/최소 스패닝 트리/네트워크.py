import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
parent = [i for i in range(n+1)]

edges = []
for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))


def find_set(x):
    if parent[x] == x:
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


edges.sort()

total_cost = 0
for cost, aa, bb in edges:
    if find_set(aa) != find_set(bb):
        union_set(aa, bb)
        total_cost += cost

print(total_cost)
