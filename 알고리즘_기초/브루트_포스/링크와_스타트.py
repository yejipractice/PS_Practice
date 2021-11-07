from itertools import combinations
import sys
input = sys.stdin.readline

n = int(input())
board = [[0]*(n+1)]
for _ in range(n):
    in1 = [0]
    in2 = list(map(int, input().split()))
    board.append(in1 + in2)

people = [i for i in range(1, n+1)]
cases = []
# 인원수
for i in range(1, n//2+1):
    case = list(combinations(people, i))
    cases.extend(case)


def check_score(array):
    sum = 0
    ccases = list(combinations(array, 2))
    for cc in ccases:
        a, b = cc
        if board[a][b] == 0 or board[b][a] == 0:
            continue
        sum += (board[a][b]+board[b][a])
    return sum


min_score = 100*n*n
for case in cases:
    new = []
    for c in case:
        new.append(c)
    another = list(set(people)-set(new))  # 배열 간 빼기
    ns = check_score(new)
    cs = check_score(another)
    min_score = min(min_score, abs(ns-cs))

print(min_score)
