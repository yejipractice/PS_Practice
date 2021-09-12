import sys
input = sys.stdin.readline


def gcd(a, b):  # 최대공약수
    while b != 0:
        c = a % b
        a = b
        b = c
    return a


def lcm(a, b):  # 최소공배수
    baesu = (a*b) / gcd(a, b)
    return baesu


N = int(input())
for _ in range(N):
    a, b = map(int, input().split())
    print(int(lcm(a, b)))
