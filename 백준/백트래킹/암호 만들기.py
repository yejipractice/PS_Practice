import copy

aei = ["a", "e", "i", "o", "u"]
# a in "aeiou" 가능

l, c = map(int, input().split())
alphas = list(map(str, input().split()))
alphas.sort()


def check(array):  # 배열간 원소 제거
    if len(list(set(aei)-set(array))) == 5:
        return False
    if len(list(set(array)-set(aei))) < 2:
        return False
    return True


def dfs(start, array):
    if len(array) == l:
        if check(array):
            print(*array, sep="")
        return
    for i in range(start, len(alphas)):
        new = copy.deepcopy(array)
        new.append(alphas[i])
        dfs(i+1, new)


dfs(0, [])
