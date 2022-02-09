import sys
sys.setrecursionlimit(10**5)  # 재귀 호줄 제한 늘리기
n = int(input())

graph = [[] for i in range(n+1)]

for _ in range(n-1):
    a, b, cost = map(int, input().split())
    graph[a].append((b, cost))
    graph[b].append((a, cost))

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


# 루트 1부터 최단 말단 찾은 다음 그 노드로부터 최장 경로 찾기 (dfs 2번)
# 더 나은 방법 강구해보기 ㅠㅠ
