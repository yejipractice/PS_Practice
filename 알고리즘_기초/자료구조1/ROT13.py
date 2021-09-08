import sys
input = sys.stdin.readline

lower = "abcdefghijklmnopqrstuvwxyz"
upper = lower.upper()
n = len(lower)
sentence = input().rstrip("\n")
answer = []

for s in sentence:
    if s.isupper():
        idx = upper.index(s)
        if idx + 13 < n:
            idx = idx + 13
        else:
            idx = idx + 13 - n
        answer.append(upper[idx])
    elif s.islower():
        idx = lower.index(s)
        if idx + 13 < n:
            idx = idx + 13
        else:
            idx = idx + 13 - n
        answer.append(lower[idx])
    else:
        answer.append(s)

print(*answer, sep="")
