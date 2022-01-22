n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()


def dfs(start, array):
    if len(array) == m:
        print(*array)
        return
    for i in range(start, n):
        if nums[i] not in array:
            dfs(i+1, array+[nums[i]])


dfs(0, [])
