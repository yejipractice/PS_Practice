n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
selected = [0]*n


def dfs(array):
    if len(array) == m:
        print(*array)
    for i in range(n):
        if selected[i] == 0:
            array.append(nums[i])
            selected[i] = 1
            dfs(array)
            selected[i] = 0
            array.pop()


dfs([])
