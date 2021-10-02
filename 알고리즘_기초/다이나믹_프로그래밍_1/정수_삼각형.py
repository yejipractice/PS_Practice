import sys
input = sys.stdin.readline

n = int(input())
nums = [0]
for _ in range(n):
    ns = [0]
    ns.extend(list(map(int, input().split())))
    nums.append(ns)

if n == 1:
    print(nums[1][1])
elif n > 1:
    nums[2][1] += nums[1][1]
    nums[2][2] += nums[1][1]
    for i in range(3, n+1):
        nums[i][1] += nums[i-1][1]
        for j in range(2, i):
            nums[i][j] += max(nums[i-1][j-1], nums[i-1][j])
        nums[i][i] += nums[i-1][i-1]

    print(max(nums[n]))
