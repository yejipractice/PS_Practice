N = int(input())


five = N // 5
three = (N-five*5) // 3

result = -1

while(True):
    if five < 0 or three < 0:
        break

    if five*5 + three*3 == N:
        result = five + three
        break

    five -= 1
    three = (N-five*5) // 3

print(result)
