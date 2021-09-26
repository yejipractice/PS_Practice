import sys
input = sys.stdin.readline

n = int(input())

# 9 90 900 9000 90000 900000
nums = [0]*(10+1)

for i in range(1, 10+1):
    nums[i] = 9*10**(i-1)

size = len(str(n))

sum = 0
for i in range(1, size):
    sum += i*nums[i]

sum += (n-10**(size-1)+1)*size

print(sum)
