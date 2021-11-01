from itertools import permutations
import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))

answer = 0
array = list(permutations(nums, n))
for i in range(len(array)):
    ans = 0
    for j in range(1, len(array[i])):
        ans += abs(array[i][j-1] - array[i][j])
    answer = max(ans, answer)

print(answer)
