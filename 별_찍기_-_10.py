n = int(input())
n = n**(1/3)


def func(n):
    if n == 1:
        print("***")
    else:
        return func(n-1)
