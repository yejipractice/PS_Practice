import sys
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    answer = -1
    m, n, x, y = map(int, input().split())
    for i in range(x, m*n, m):  # 시간 줄이기 위한 범위 잡는 것이 핵심 << 경우의 수 줄이기
        if (i-x) % m == 0 and (i-y) % n == 0:
            answer = i
            break
    print(answer)
