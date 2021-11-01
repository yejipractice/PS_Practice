from itertools import permutations

n = int(input())
nums = [x for x in range(1, n+1)]

array = list(permutations(nums, n))

for a in array:
    print(*a)
