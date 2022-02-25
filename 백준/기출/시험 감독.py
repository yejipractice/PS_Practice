import sys
input = sys.stdin.readline

n = int(input())
classes = list(map(int, input().split()))
b, c = map(int, input().split())

answer = 0
for one in classes:
    one -= b
    answer += 1
    if one > 0:
        answer += one // c
        if one % c != 0:
            answer += 1

print(answer)
