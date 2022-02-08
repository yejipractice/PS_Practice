n, m = map(int, input().split())
parent = [i for i in range(n+1)]


def find_set(x):
    if parent[x] != x:
        return find_set(parent[x])
    return x


def union_set(x, y):
    a = find_set(x)
    b = find_set(y)
    if a != b:
        parent[b] = a


for _ in range(m):
    a, b = map(int, input().split())
    union_set(a, b)

res = []
for i in range(1, n+1):
    p = find_set(i)
    if not p in res:  # parent 갱신 누락 있으므로 find_set 기준으로 해야 한다 잊지 않기
        res.append(p)

print(len(res))
