import sys
input = sys.stdin.readline

n = int(input())
a, b = map(int, input().split())
graph = [[] for _ in range(n+1)]


for _ in range(int(input())):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)


def bfs(x, y):
    queue = set()
    queue.add((x, 0))
    visited = [False for i in range(n+1)]
    visited[x] = True
    while queue:
        now, relation = queue.pop()
        visited[now] = True
        if now == y:
            return relation
        for next in graph[now]:
            if visited[next] == False:
                queue.add((next, relation+1))
    return -1


print(bfs(a, b))
