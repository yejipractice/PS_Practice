import sys
input = sys.stdin.readline

stack = []

N = int(input())

for _ in range(N):
    word = input().rstrip()
    if "push" in word:
        stack.append(int(word[5:]))

    elif word == "top":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])

    elif word == "empty":
        if len(stack) == 0:
            print(1)
        else:
            print(0)

    elif word == "size":
        print(len(stack))

    elif word == "pop":
        if len(stack) == 0:
            print(-1)
        else:
            n = stack.pop()
            print(n)
