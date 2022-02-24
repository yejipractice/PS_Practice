import sys
input = sys.stdin.readline


def bfs(node):
    queue = set()
    if visited[node] == 0:
        visited[node] = 1
    queue.add((node, visited[node]))
    while queue:
        now, mark = queue.pop()
        visited[now] = mark
        for next in graph[now]:
            if visited[next] == mark:
                return False
            if visited[next] == 0:
                if mark == 1:
                    queue.add((next, -1))
                else:
                    queue.add((next, 1))
    return True


for tc in range(int(input())):
    v, e = map(int, input().split())
    visited = [0 for i in range(v+1)]
    graph = [[] for _ in range(v+1)]
    for _ in range(e):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    answer = "YES"
    for idx in range(1, v+1):  # 연결 그래프가 아니므로 모든 인덱스에 대해 확인해야 함
        if bfs(idx) == False:
            answer = "NO"
    print(answer)


# 이분 그래프 정의
# https://hongcoding.tistory.com/20
