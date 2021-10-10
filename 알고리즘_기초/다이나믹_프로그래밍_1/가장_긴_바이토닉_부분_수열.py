import sys
input = sys.stdin.readline

n = int(input())

nums = list(map(int, input().split()))


def find_max(array):
    nn = len(array)
    d = [1 for i in range(nn)]
    for i in range(nn):
        for j in range(i):
            if array[i] > array[j]:
                d[i] = max(d[i], d[j]+1)
    return d


def find_min(array):
    nn = len(array)
    d = [1 for i in range(nn)]
    for i in range(nn-1, -1, -1):
        for j in range(nn-1, i, -1):
            if array[i] > array[j]:
                d[i] = max(d[i], d[j]+1)
    return d


inc = find_max(nums)
dc = find_min(nums)
result = [0] * n
for i in range(n):
    result[i] = inc[i]+dc[i]-1

print(max(result))
