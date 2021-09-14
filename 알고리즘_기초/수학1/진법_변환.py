n, num = input().split()
num = int(num)

idx = len(n)-1

res = 0

alpha = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

for i in n:
    res += alpha.index(i)*(num**idx)
    idx -= 1

print(res)
