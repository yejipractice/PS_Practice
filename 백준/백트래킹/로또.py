import copy


def dfs(line, answer, start):
    if len(answer) == 6:
        print(*answer)
        return
    for i in range(start, len(line)):
        new = copy.deepcopy(answer)
        new.append(line[i])
        dfs(line, new, i+1)


while True:
    line = list(map(int, input().split()))
    if line[0] == 0:
        break
    n = line.pop(0)
    dfs(line, [], 0)
    print()
