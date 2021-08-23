n = int(input())
inputs = list(map(int, input().split()))

count = n

for inp in inputs:
    if inp == 1:
        count -= 1
        continue
    for i in range(2, inp):
        if inp % i == 0:
            count -= 1
            break

print(count)
