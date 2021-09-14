n, num = input().split()
num = int(num)

idx = len(n)-1

res = 0

while idx >= 0:
    r = n[idx]
    if not r.isdigit():
        r = ord(r)-ord("A")+10
    res += (num**idx)*r
    idx -= 1
print(res)
