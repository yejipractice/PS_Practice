from collections import deque

INF = float('inf')

for _ in range(int(input())):
    n, m = map(int, input().split())
    distances = [[INF for i in range(n+1)]for j in range(n+1)]    
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        a, b, c = map(int, input().split())
        graph[a].append((b, c))
        graph[b].append((a, c))
    for i in range(n+1):
        distances[i][i] = 0
    for now in range(1, n+1):
        queue = deque()
        for b, c in graph[now]:
            queue.append((b, c))
        while queue:
            next, cost = queue.popleft()
            if cost < distances[now][next]:
                distances[now][next] = cost
                for nextnext, nn_cost in graph[next]:
                    queue.append((nextnext, cost+nn_cost))
    friend_cnt = int(input())
    friends = list(map(int, input().split()))
    answer = -1
    distance_sum = INF
    for node in range(1, n+1):
        node_sum = 0
        for friend in friends:
            node_sum+= distances[friend][node]
        if node_sum < distance_sum:
            distance_sum = node_sum
            answer = node
    print(answer)