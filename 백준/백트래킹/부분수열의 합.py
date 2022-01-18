import copy

n, s = map(int, input().split())
nums = list(map(int, input().split()))
answer = 0


def dfs(array, start):
    global answer
    if array != [] and sum(array) == s:
        answer += 1
    if start >= n:
        return
    for i in range(start, len(nums)):
        new = copy.deepcopy(array)
        new.append(nums[i])
        dfs(new, i+1)


dfs([], 0)
print(answer)
