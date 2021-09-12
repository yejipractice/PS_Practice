import math
import sys
input = sys.stdin.readline

n, m = map(int, input().split())


def countNum(n, num):
    count = 0
    div = num
    while(n >= div):
        count += (n//div)
        div *= num
    return count


print(min(countNum(n, 5) - countNum(m, 5) - countNum(n-m, 5),
      countNum(n, 2) - countNum(m, 2) - countNum(n-m, 2)))
