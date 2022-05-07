import sys
input = sys.stdin.readline

r, c, k = map(int, input().split())
graph = []
for _ in range(3):
    graph.append(list(map(int, input().split())))
time = 0


def put_zero(graph, n):
    for idx in range(len(graph)):
        if len(graph[idx]) < n:
            for i in range(n-len(graph[idx])):
                graph[idx].append(0)
    return graph


def r_op(graph):
    tmp_graph = []
    max_n = 0
    for ridx in range(min(len(graph), 100)):
        tmp = []
        stores = dict()
        for cidx in range(min(100, len(graph[ridx]))):
            if stores.get(graph[ridx][cidx], False) == False:
                stores[graph[ridx][cidx]] = 1
            else:
                stores[graph[ridx][cidx]] += 1
        for node in stores.keys():
            tmp.append((node, stores[node]))
        tmp.sort(key=lambda x: (x[1], x[0]))
        tg = []
        for number, cnt in tmp:
            if number == 0:
                continue
            tg.append(number)
            tg.append(cnt)
        max_n = max(max_n, len(tg))
        tmp_graph.append(tg)
    tmp_graph = put_zero(tmp_graph, max_n)
    return tmp_graph


def reverse(graph):
    tmp_graph = []
    for cidx in range(len(graph[0])):
        tmp = []
        for ridx in range(len(graph)):
            tmp.append(graph[ridx][cidx])
        tmp_graph.append(tmp)
    return tmp_graph


def c_op(graph):
    tmp_graph = []
    max_n = 0
    for cidx in range(min(len(graph[0]), 100)):
        tmp = []
        stores = dict()
        for ridx in range(min(len(graph), 100)):
            if stores.get(graph[ridx][cidx], False) == False:
                stores[graph[ridx][cidx]] = 1
            else:
                stores[graph[ridx][cidx]] += 1
        for node in stores.keys():
            tmp.append((node, stores[node]))
            tmp.sort(key=lambda x: (x[1], x[0]))
        tg = []
        for number, cnt in tmp:
            if number == 0:
                continue
            tg.append(number)
            tg.append(cnt)
        max_n = max(max_n, len(tg))
        tmp_graph.append(tg)
    tmp_graph = put_zero(tmp_graph, max_n)
    tmp_graph = reverse(tmp_graph)
    return tmp_graph


while 1:
    if len(graph) > r-1 and len(graph[0]) > c-1:
        if graph[r-1][c-1] == k:
            break
    if time >= 100:
        time = -1
        break
    if len(graph) >= len(graph[0]):
        graph = r_op(graph)
        time += 1
    else:
        graph = c_op(graph)
        time += 1

print(time)
