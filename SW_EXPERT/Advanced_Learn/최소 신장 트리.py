
def Make_Set(p, v):
    p[v] = v


def Find_Set(p, v):
    if p[v] != v:
        return Find_Set(p, p[v])
    return p[v]


def union_set(p, n1, n2):
    p[Find_Set(p, n1)] = Find_Set(p, n2)


# 크루스칼 알고리즘
for tc in range(1, int(input())+1):
    edges = []
    result = []
    v, e = map(int, input().split())
    for _ in range(e):
        n1, n2, w = map(int, input().split())
        edges.append((w, n1, n2))
    edges.sort()
    visited = [i for i in range(0, v+1)]
    totalCost = 0

    while len(result) < v:
        cost, one, other = edges.pop(0)
        if Find_Set(visited, one) != Find_Set(visited, other):
            union_set(visited, one, other)
            result.append((one, other))
            totalCost += cost

    print("#"+str(tc)+" "+str(totalCost))
