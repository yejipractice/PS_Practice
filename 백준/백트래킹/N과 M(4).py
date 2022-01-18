import copy

n, m = map(int, input().split())
nums = [i for i in range(1, n+1)]


def dfs(start, ans):
    if len(ans) == m:
        print(*ans)
        return
    for idx in range(start, len(nums)):
        new = copy.deepcopy(ans)
        new.append(nums[idx])
        dfs(idx, new)


dfs(0, [])
