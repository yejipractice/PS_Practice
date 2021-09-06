import sys
input = sys.stdin.readline

alpah = "abcdefghijklmnopqrstuvwxyz"
counts = [0] * len(alpah)

sentence = input().strip()
for s in sentence:
    counts[alpah.index(s)] += 1

print(*counts)
