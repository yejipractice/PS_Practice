from itertools import permutations
import sys
input = sys.stdin.readline

INF = 1000000+1

n = int(input())
costs = []
for _ in range(n):
    costs.append(list(map(int, input().split())))
nums = [x for x in range(1, n+1)]
cases = list(permutations(nums, n))

answer = INF * n
for case in cases:
    sum = 0
    for i in range(len(case)):
        if i == len(case)-1:
            a = case[i]
            b = case[0]
        else:
            a = case[i]
            b = case[i+1]
        if costs[a-1][b-1] == 0:  # 0인 경우(이동 못하는 경우) 고려해주기
            costs[a-1][b-1] = INF
        sum += costs[a-1][b-1]
    answer = min(answer, sum)

print(answer)
