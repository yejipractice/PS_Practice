from itertools import product
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = [i for i in range(1, n+1)]

a = product(nums, repeat=m)
answer = []

for i in a:
    i = list(i)
    i.sort()
    if i not in answer:
        answer.append(i)

for i in answer:
    print(*i)
