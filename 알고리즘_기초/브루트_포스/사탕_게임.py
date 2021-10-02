import sys
input = sys.stdin.readline

n = int(input())
candies = []
for _ in range(n):
    candies.append(list(input().rstrip('\n')))


def width():
    result = 0
    for i in range(n):
        count = 1
        for j in range(n-1):
            if candies[i][j] == candies[i][j+1]:
                count += 1
            else:
                result = max(count, result)
                count = 1
            result = max(count, result)
    return result


def height():
    result = 0
    for i in range(n):
        count = 1
        for j in range(n-1):
            if candies[j][i] == candies[j+1][i]:
                count += 1
            else:
                result = max(count, result)
                count = 1
            result = max(count, result)
    return result


m = 0
break_p = 0

hh = height()
ww = width()
m = max(m, hh)
m = max(m, ww)

for i in range(n):
    if break_p == 1:
        break
    for j in range(n-1):
        if m == n:
            break_p = 1
            break
        if candies[i][j] != candies[i][j+1]:
            candies[i][j], candies[i][j+1] = candies[i][j+1], candies[i][j]
            h = height()
            w = width()
            m = max(m, h)
            m = max(m, w)
            candies[i][j], candies[i][j+1] = candies[i][j+1], candies[i][j]

for i in range(n):
    for j in range(n-1):
        if candies[j][i] != candies[j+1][i]:
            candies[j][i], candies[j+1][i] = candies[j+1][i], candies[j][i]
            h = height()
            w = width()
            m = max(m, h)
            m = max(m, w)
            candies[j][i], candies[j+1][i] = candies[j+1][i], candies[j][i]

print(m)
