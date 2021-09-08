import sys
input = sys.stdin.readline

word = input().rstrip("\n")
n = len(word)
answer = []

for i in range(n):
    w = word[i:]
    answer.append(w)

answer.sort()

print(*answer, sep="\n")
