def make_set(x):
    parent[x] = x


def find_set(x):
    if parent[x] == x:
        return x
    return find_set(parent[x])


def union_set(x, y):
    a = find_set(x)
    b = find_set(y)
    if a != b:
        parent[b] = a

# 1번 컴퓨터와 연결 여부를 트리(부모노드 연결 여부)로 판단


n = int(input())
m = int(input())

parent = [0] * (n+1)

for node in range(1, n+1):
    make_set(node)

for _ in range(m):
    a, b = map(int, input().split())
    union_set(a, b)

cnt = 0
for node in range(2, n+1):
    if find_set(node) == find_set(1):  # 바로 parent로 비교하면 오답
        cnt += 1  # find_set 함수를 통해 비교해야 한다

print(cnt)
