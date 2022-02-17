import sys
input = sys.stdin.readline

graph = []
for _ in range(5):
    graph.append(list(map(int, input().split())))

dic = set()


def dfs(x, y, word):
    if len(word) == 6:
        dic.add(word)
        return
    for xx, yy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        dx, dy = x+xx, y+yy
        if 0 <= dx < 5 and 0 <= dy < 5:
            dfs(dx, dy, word+str(graph[dx][dy]))


for i in range(5):
    for j in range(5):
        dfs(i, j, "")

print(len(dic))
