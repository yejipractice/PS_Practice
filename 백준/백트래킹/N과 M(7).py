n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()


def dfs(array):
    if len(array) == m:
        print(*array)
        return
    for num in nums:
        dfs(array+[num])


dfs([])
