from itertools import combinations
import sys
input = sys.stdin.readline

n, c = map(int, input().split())
alpha = list(map(str, input().split()))
a = "aeiou"
aalpha = [x for x in alpha if x in a]
noalpha = [x for x in alpha if x not in a]

ans = []
for i in range(1, len(aalpha)+1):
    aa = list(combinations(aalpha, i))
    if n-i < 2:  # 자음 모음 개수 조건 둘다 체크하기
        continue
    bb = list(combinations(noalpha, n-i))
    for ii in range(len(aa)):
        for jj in range(len(bb)):
            ans.append(sorted(aa[ii]+bb[jj]))
ans.sort()
for i in ans:
    print("".join(i))
