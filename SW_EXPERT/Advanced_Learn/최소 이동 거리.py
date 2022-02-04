INF = float('inf')

cases = [[0, 1], [0, -1], [1, 0], [-1, 0]]

for tc in range(1, int(input())+1):
    n, e = map(int, input().split())
    graph = [INF] * (n+1)
    graph[0] = 0
    for _ in range(e):
        a, b, w = map(int, input().split())
        graph[b] = min(graph[a]+w, graph[b])
    print("#"+str(tc), end=" ")
    print(graph[-1])

# 입력    출력
# 2 3     #1 2
# 0 1 1
# 0 2 6
# 1 2 1

# 플로이드 워셜 알고리즘 -> 시간초과

# INF = float('inf')

# for tc in range(1, int(input())+1):
#     n, e = map(int, input().split())
#     graph = [[INF for i in range(n+1)] for j in range(n+1)]
#     for idx in range(n+1):
#         graph[idx][idx] = 0
#     for _ in range(e):
#         a, b, w = map(int, input().split())
#         graph[a][b] = w
#     for k in range(n+1):
#         for start in range(n+1):
#             for end in range(n+1):
#                 graph[start][end] = min(
#                     graph[start][end], graph[start][k]+graph[k][end])
#     print("#"+str(tc), end=" ")
#     print(graph[0][n])
