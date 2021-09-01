import sys
input = sys.stdin.readline

word = list(map(str, input().strip()))

N = int(input())

cs = len(word)

for _ in range(N):
    inputs = input().strip()
    if inputs == "L":
        if cs > 0:
            cs -= 1
    elif inputs == "D":
        if cs < len(word):
            cs += 1
    elif inputs == "B":
        if cs != 0:
            word.remove(word[cs-1])
            cs -= 1
    else:
        alpha = inputs[-1]
        if cs == len(word):
            word.append(alpha)
            cs += 1
        else:
            word.insert(cs, alpha)
            cs += 1

print("".join(word))

# 시간 초과 => 스택 사용해서 다시 풀어보기
