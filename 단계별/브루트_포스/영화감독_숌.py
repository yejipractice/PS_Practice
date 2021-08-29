INF = 10000**2

n = int(input())

list = []

for i in range(INF):
    if '666' in str(i):
        list.append(i)
    if len(list) >= n:
        break

print(list[-1])
