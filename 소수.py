m = int(input())
n = int(input())

result = []

for num in range(m, n+1):
    if num == 1:
        continue
    if num == 2:
        result.append(num)
    for i in range(2, num):
        if num % i == 0:
            break
        if i == num-1:
            result.append(num)

if result == []:
    min = -1
    print(min)
else:
    min = result[0]
    print(sum(result))
    print(min)
