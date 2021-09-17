import sys
input = sys.stdin.readline

n = int(input())
nums = []
for _ in range(n):
    nums.append(int(input()))

max_num = max(nums)

memo = [[]] * (max_num+1)
memo[1] = [[1]]
memo[2] = [[2]]
memo[3] = [[1, 2], [2, 1], [3]]

for i in range(4, max_num+1):
    r = []
    for j in range(1, i):
        for ii in memo[j]:
            for jj in memo[i-j]:
                if ii[-1] != jj[0]:
                    newL = ii+jj
                    if r.count(newL) == 0:
                        r.append(newL)
    memo[i] = r

for i in nums:
    print(len(memo[i]))
