import sys

# sys.stdin = open("input.txt", "r")

for tc in range(1, 10+1):
    n = int(input())
    lines = list(map(int, input().split()))
    opes_num = int(input())
    opes = list(map(str, input().split()))
    count = 0
    while 1:
        if count == opes_num:
            break
        ope = opes.pop(0)
        if ope == "I":
            x = int(opes.pop(0))
            y = int(opes.pop(0))
            s = []
            for j in range(y):
                lines.insert(x+j, int(opes.pop(0)))
        elif ope == "D":
            x = int(opes.pop(0))
            y = int(opes.pop(0))
            for _ in range(y):
                lines.pop(x+1)
        elif ope == "A":
            y = int(opes.pop(0))
            s = []
            for _ in range(y):
                s.append(int(opes.pop(0)))
            lines += s
        count += 1
    print("#"+str(tc), end=" ")
    print(*lines[:10])

# 파이썬 배열의 insert 함수 사용하기
