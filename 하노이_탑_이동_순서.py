N = int(input())


answer = []


def hanoi(n, start, assist, end):
    if n == 1:
        answer.append([start, end])
        return
    else:
        hanoi(n-1, start, end, assist)
        answer.append([start, end])
        hanoi(n-1, assist, start, end)


hanoi(N, 1, 2, 3)
print(len(answer))
for i in answer:
    print(i[0], i[1])
