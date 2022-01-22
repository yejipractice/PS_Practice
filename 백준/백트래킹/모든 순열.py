n = int(input())
selected = [0]*(n+1)


def dfs(array):
    if len(array) == n:
        print(*array)
        return
    for i in range(1, n+1):
        if selected[i] == 0:
            selected[i] = 1
            array.append(i)
            dfs(array)
            array.pop()
            selected[i] = 0


dfs([])
