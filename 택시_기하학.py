import math
r = int(input())
PI = math.pi

circle = round(PI * r * r, 6)
taxi = 2 * r * r

print(circle)
print("{:.6f}".format(taxi))  # 소수점 표현
