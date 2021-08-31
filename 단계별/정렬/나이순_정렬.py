import sys
input = sys.stdin.readline

N = int(input())

inputs = []
for _ in range(N):
    age, name = input().split()
    inputs.append([int(age), name])

inputs.sort(key=lambda x: x[0])

for i in inputs:
    print(i[0], i[1])
