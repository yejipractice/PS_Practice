def find_set(parent, x):
    if parent[x] != x:
        parent[x] = find_set(parent, parent[x])
    return parent[x]

def union_set(parent, x, y):
    parent[find_set(parent, x)] = parent[find_set(parent, y)]

def solution(n, computers):
    answer = 0
    parent = [i for i in range(n+1)]
    for i in range(n):
        for j in range(n):
            if i != j and computers[i][j]==1:
                union_set(parent, i+1, j+1)
    for i in range(1, n+1):
        find_set(parent, i)
    answer = set()
    for i in range(1, n+1):
        answer.add(parent[i])
    return len(answer)