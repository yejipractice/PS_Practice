import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

n = int(input())
graph = [[] for i in range(n+1)]

for _ in range(n-1):
    a, b, w = map(int, input().split())
    graph[a].append((b, w))
    graph[b].append((a, w))

arr = []
for node in range(1, n+1):
    if len(graph[node]) == 1:
        arr.append(node)

answer = 0
idx = -1


def dfs(x, sum, visited):
    global answer, idx
    if sum > answer:
        answer = sum
        idx = x
    visited[x] = 1
    for next, ww in graph[x]:
        if visited[next] == 0:
            visited[next] = 1
            dfs(next, sum+ww, visited)
            visited[next] = 0


visited = [0 for i in range(n+1)]
dfs(1, 0, visited)

visited = [0 for i in range(n+1)]
dfs(idx, 0, visited)

print(answer)

# bfs -> dfs : visited 시간 초과
# 최후 말단 중 dfs => 루트로부터 최장 최후 말단 dfs로 구해서 전체적으로 dfs # 핵심 가지치기
