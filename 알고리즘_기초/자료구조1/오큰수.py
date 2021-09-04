import sys
input = sys.stdin.readline

N = int(input())
answer = [-1] * N
nums = list(map(int, input().split()))
stack = [0]

for i in range(1, N):
    while stack and nums[stack[-1]] < nums[i]:
        answer[stack.pop()] = nums[i]
    stack.append(i)

# 1번째 index부터 앞의 수와 비교해나가기 해당되지 않을 때 index를 stack에 넣고 다음 턴에 비교
