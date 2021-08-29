from typing import Tuple


END = 10000
sieve = [True] * (END+1)
n = int(input())


def prime(x):
    for i in range(2, x+1):
        if sieve[i] == True:
            for j in range(i+i, END+1, i):
                sieve[j] = False


for _ in range(n):
    num = int(input())
    x = int(num**0.5)
    prime(x)

    for i in range(num//2, num):
        if sieve[i] == True and sieve[num-i] == True:
            a = i
            b = num-i
            break
    print(b, a)
