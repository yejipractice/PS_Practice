import sys
input = sys.stdin.readline

alpha = "abcdefghijklmnopqrstuvwxyz"
counts = [-1] * len(alpha)

sentence = input().strip()
for i in range(len(sentence)):
    if counts[alpha.index(sentence[i])] == -1:
        counts[alpha.index(sentence[i])] = i

print(*counts)
