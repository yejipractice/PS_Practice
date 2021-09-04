import sys
input = sys.stdin.readline

N = int(input())

nums = list(map(int, input().split()))

for i in range(N):
    num = nums[i]
    answer = -1
    for j in range(i+1, N):
        if nums[j] > num:
            answer = nums[j]
            break
    print(answer, end=" ")

# 시간 초과
