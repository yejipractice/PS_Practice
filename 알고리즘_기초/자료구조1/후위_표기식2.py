import sys
input = sys.stdin.readline

N = int(input())
sentence = input().strip()
alpha = []
for i in range(N):
    alpha.append(int(input()))

stack = []
for s in sentence:
    if s.isalpha():
        stack.append(alpha[ord(s)-ord('A')])
    else:
        n2 = stack.pop()
        n1 = stack.pop()
        if s == "+":
            stack.append(n1+n2)
        elif s == "-":
            stack.append(n1-n2)
        elif s == "*":
            stack.append(n1*n2)
        elif s == "/":
            stack.append(n1/n2)

print(format(stack[0], ".2f"))
