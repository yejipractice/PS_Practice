n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()


def dfs(array):
    if len(array) == m:
        print(*array)
        return
    for num in nums:
        if len(array) == 0 or array[-1] <= num:
            array.append(num)
            dfs(array)
            array.pop()


dfs([])
