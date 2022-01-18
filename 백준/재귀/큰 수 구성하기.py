n, k = map(int, input().split())
nums = list(map(int, input().split()))
MAX = -1


def check(ans):
    global MAX
    for num in nums:
        new = ans+[num]
        if int("".join(list((map(str, new))))) <= n:
            MAX = max(MAX, int("".join(list((map(str, new))))))
            check(new)


ans = []
check(ans)
print(MAX)
