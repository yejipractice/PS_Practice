from itertools import combinations
import sys
input = sys.stdin.readline

n = int(input())
costs = []
for _ in range(n):
    costs.append(list(map(int, input().split())))
nums = [x for x in range(1, n+1)]
cases = list(combinations(nums, n//2))

ans = 101*n*2
for case in cases:
    start = case
    link = [x for x in range(1, n+1) if x not in case]
    start_score = 0
    link_score = 0

    for s in list(combinations(start, 2)):
        a, b = s
        start_score += (costs[a-1][b-1] + costs[b-1][a-1])

    for l in list(combinations(link, 2)):
        a, b = l
        link_score += (costs[a-1][b-1] + costs[b-1][a-1])

    ans = min(ans, abs(start_score - link_score))

print(ans)
