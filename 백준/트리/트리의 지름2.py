import sys
sys.setrecursionlimit(10**5)

n = int(input())

graph = [[] for _ in range(n+1)]

for _ in range(n):
    inputs = list(map(int, input().split()))
    node = inputs[0]
    for idx in range(1, len(inputs)-1, 2):
        graph[node].append((inputs[idx], inputs[idx+1]))
        graph[inputs[idx]].append((node, inputs[idx+1]))

max_num = 0
idx = -1


def dfs(node, sum, visited):
    global max_num, idx
    if sum > max_num:
        max_num = sum
        idx = node
    visited[node] = 1
    for next, cost in graph[node]:
        if visited[next] == 0:
            visited[next] = 1
            dfs(next, sum+cost, visited)
            visited[next] = 0


visited = [0 for i in range(n+1)]
dfs(1, 0, visited)

visited = [0 for i in range(n+1)]
max_num = 0
dfs(idx, 0, visited)
print(max_num)
