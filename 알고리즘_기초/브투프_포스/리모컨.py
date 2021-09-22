import sys
input = sys.stdin.readline

channel = int(input())
n = int(input())
delete = list(input().strip())


def check(num):
    for n in list(str(num)):
        if n in delete:
            return False
    return True


answer = abs(100-channel)
for i in range(500000*2+1):
    if check(i):
        answer = min(abs(i-channel)+len(str(i)), answer)

print(answer)
