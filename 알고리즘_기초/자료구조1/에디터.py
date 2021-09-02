import sys
input = sys.stdin.readline

word = list(map(str, input().strip()))
container = []

N = int(input())


for _ in range(N):
    cs = len(word)
    inputs = input().strip()
    if inputs == "L":
        if cs > 0:
            a = word.pop()
            container.append(a)
    elif inputs == "D":
        if len(container) > 0:
            a = container.pop()
            word.append(a)
    elif inputs == "B":
        if cs > 0:
            word.pop()
    else:
        alpha = inputs[-1]
        word.append(alpha)

for _ in range(len(container)):
    i = container.pop()
    word.append(i)

print("".join(word))

# 스택과 배열이용의 시간 차이?
