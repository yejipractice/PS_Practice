import sys
input = sys.stdin.readline

N = int(input())

solution = []
for _ in range(N):
    solution.append(int(input()))

container = []
index = 0
isSol = []
answers = []

for i in range(1, N+1):
    container.append(i)
    answers.append("+")
    while(container[-1] == solution[index]):
        pop_num = container.pop()
        answers.append("-")
        isSol.append(pop_num)
        index += 1
        if len(container) == 0:
            break

if len(solution) != len(isSol):
    print("NO")
else:
    for i in answers:
        print(i)
