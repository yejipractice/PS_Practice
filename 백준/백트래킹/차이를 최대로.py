n = int(input())
lines = [0]+list(map(int, input().split()))
selected = [0] * (n+1)
max_sum = -1


def check(array):
    global max_sum
    sum = 0
    for idx in range(len(array)-1):
        res = abs(lines[array[idx]]-lines[array[idx+1]])
        sum += res
    max_sum = max(max_sum, sum)


def dfs(array):
    if len(array) == n:
        check(array)
        return
    for i in range(1, n+1):
        if selected[i] == 0:
            selected[i] = 1
            array.append(i)
            dfs(array)
            array.pop()
            selected[i] = 0


dfs([])
print(max_sum)
