import sys
input = sys.stdin.readline

N = int(input())

for _ in range(N):
    sentence = list(map(str, input().split()))
    for word in sentence:
        print("".join(list(reversed(word))), end=" ")
    print()
