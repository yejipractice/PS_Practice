import sys
input = sys.stdin.readline
sys.setrecursionlimit(10*5)

n = int(input())
graph = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]
dis = [0 for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def dfs(node):
    visited[node] = True
    for next in graph[node]:
        if visited[next] == False:
            dis[next] = dis[node]+1
            dfs(next)


dfs(1)

answer = 0
for idx in range(2, n+1):
    if len(graph[idx]) == 1:
        answer += dis[idx]

print("No" if answer % 2 == 0 else "Yes")
