import sys
from typing import Counter
input = sys.stdin.readline

N = int(input())
answer = [-1] * N
nums = list(map(int, input().split()))
stack = [0]
counts = Counter(nums)

for i in range(1, N):
    while stack and counts[nums[stack[-1]]] < counts[nums[i]]:
        answer[stack.pop()] = nums[i]
    stack.append(i)

print(*answer)
