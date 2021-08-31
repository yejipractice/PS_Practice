import sys
input = sys.stdin.readline

N = int(input())

nums = list(map(int, input().split()))

ranks = sorted(list(set(nums)))

dics = {}

# 딕셔너리 사용법
for i in range(len(ranks)):
    dics[ranks[i]] = i

for i in range(N):
    nums[i] = dics[nums[i]]

# 배열 값만 출력
print(*nums)
