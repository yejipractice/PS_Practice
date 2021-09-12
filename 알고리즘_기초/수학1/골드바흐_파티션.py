import sys
input = sys.stdin.readline

time = int(input())
nums = [int(input()) for _ in range(time)]
INF = max(nums)

check = [False, False] + [True] * (INF-1)

for i in range(2, int(INF ** 0.5)+1):
    if check[i]:
        for j in range(i*2, INF+1, i):
            if check[j]:
                check[j] = False

for n in nums:
    count = 0
    for i in range((n//2)+1):
        if check[i] and check[n-i]:
            count += 1
    print(count)
