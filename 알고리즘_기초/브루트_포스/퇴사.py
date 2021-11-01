import sys
input = sys.stdin.readline

n = int(input())
T, P = [], []
for _ in range(n):
    t, p = map(int, input().split())
    T.append(t)
    P.append(p)
d = [0] * (n+1)

for i in range(n-1, -1, -1):
    # 퇴사일 넘기면 상담하지 않음
    if i + T[i] > n:
        d[i] = d[i+1]
    else:
        d[i] = max(d[i+1], P[i] + d[i + T[i]])

print(d[0])
