import math
import sys
input = sys.stdin.readline


N = int(input())
num = list(str(math.factorial(N)))
count = 0
while 1:
    if num.pop() != "0":
        break
    count += 1

print(count)
