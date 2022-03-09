import sys
input = sys.stdin.readline

for tc in range(1, int(input())+1):
    n, m = map(int, input().split())
    a = set()
    b = set()
    for _ in range(n):
        a.add(input().rstrip())
    for _ in range(m):
        b.add(input().rstrip())
    print("#"+str(tc), end=" ")
    print(len(a & b))  # set의 공통 부분 찾는 법
