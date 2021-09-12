import math
import sys
from itertools import combinations  # 조합 사용
input = sys.stdin.readline


n = int(input())

for _ in range(n):
    sum = 0
    nums = list(map(int, input().split()))
    all = list(combinations(nums[1:], 2))
    for i in all:
        sum += math.gcd(i[0], i[1])  # gcd 함수 사용
    print(sum)
