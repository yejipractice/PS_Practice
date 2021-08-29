import itertools


n, sum = map(int, input().split())

nums = list(map(int, input().split()))
# dis = 3000001
# result = list(itertools.combinations(nums, 3))

# for i in result:
#     s = i[0]+i[1]+i[2]
#     if s <= sum:
#         if dis >= (sum-s):
#             dis = sum-s
#             answer = s

# print(answer)

nums.sort()
m = 0
for i in range(0, n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            s = nums[i]+nums[j]+nums[k]
            if s <= sum:
                m = max(s, m)

print(m)
