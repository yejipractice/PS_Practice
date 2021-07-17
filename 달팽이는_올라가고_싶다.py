A, B, V = map(int, input().split())

# 첫 시도는 While문을 이용하였으나 시간 초과!

move = A - B
day = (V-A) // move

if (V-A) % move == 0:
    day += 1
else:
    day += 2

# day += 1 if (V-A) % move == 0 else 2

print(day)
