from collections import defaultdict
from itertools import combinations

n = int(input())

nums = list(map(int, input().split()))

box = defaultdict(list)

for comb in combinations([i for i in range(n)], 2):
    a, b = comb
    value = nums[a]+nums[b]
    box[value].append((a, b))

answer = 0
for idx in range(len(nums)):
    for a, b in box[nums[idx]]:
        if a!= idx and b!= idx:
            answer+=1
            break

print(answer)