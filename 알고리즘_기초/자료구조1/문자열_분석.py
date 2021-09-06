import sys
input = sys.stdin.readline

while 1:
    upper, lower, num, space = 0, 0, 0, 0
    sentence = input().rstrip("\n")
    if not sentence:
        break
    for s in sentence:
        if s.isupper():
            upper += 1
        elif s.islower():
            lower += 1
        elif s.isdigit():
            num += 1
        else:
            space += 1
    print(lower, upper, num, space)
