import sys
input = sys.stdin.readline

N = int(input())

nums = list(map(int, input().split()))
nums.reverse()
container = []

for i in range(N):
    num = nums.pop()
    while(True):
        if len(nums) == 0:
            print(-1, end=" ")
            for _ in range(len(container)):
                nums.append(container.pop())
            break
        else:
            next = nums.pop()
            if next > num:
                print(next, end=" ")
                nums.append(next)
                for _ in range(len(container)):
                    nums.append(container.pop())
                break
            else:
                container.append(next)

# 스택을 이용한 두 번째 시도 -> 시간 초과
