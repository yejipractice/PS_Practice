import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
graph = [[] for i in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
friends = []


def dfs(node, num):
    if node not in friends:
        friends.append(node)
    if num >= 2:
        return
    for next in graph[node]:
        dfs(next, num+1)


dfs(1, 0)
friends.remove(1)
print(len(friends))
