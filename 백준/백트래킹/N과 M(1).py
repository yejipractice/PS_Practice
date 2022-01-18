n, m = map(int, input().split())
nums = [i for i in range(1, n+1)]


def dfs(nums, answer):
    if len(answer) == m:
        print(*answer)
        return
    for i in range(len(nums)):
        new = nums.pop(i)
        answer.append(new)
        dfs(nums, answer)
        nums.append(new)
        answer.pop()
        nums.sort()


dfs(nums, [])
