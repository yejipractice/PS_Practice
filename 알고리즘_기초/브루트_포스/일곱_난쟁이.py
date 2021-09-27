import sys
input = sys.stdin.readline

h = []
for _ in range(9):
    h.append(int(input()))

s = sum(h)
break_p = 0

for i in range(8):
    if break_p == 1:
        break
    for j in range(i+1, 9):
        news = s - h[i]-h[j]
        if news == 100:
            h.pop(i)
            h.pop(j-1)
            break_p = 1
            break

h.sort()
for i in h:
    print(i)

# 파이썬 이중반복문 벗어나기 위한 변수 따로 설정
