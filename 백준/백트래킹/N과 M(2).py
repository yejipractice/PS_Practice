n, m = map(int, input().split())
nums = [i for i in range(1, n+1)]


def dfs(nums, answer):
    if len(answer) == m:
        print(*answer)
        return
    for i in range(len(nums)):
        new = nums[i]
        answer.append(new)
        dfs(nums[i+1:], answer)
        answer.pop()


dfs(nums, [])
