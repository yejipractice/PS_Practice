import sys
input = sys.stdin.readline

# 메모리 줄이는 방법
N = int(input())
result = [0]*10001


for _ in range(N):
    num = int(input())
    result[num] += 1

for i in range(1, 10001):
    for j in range(result[i]):
        print(i)
