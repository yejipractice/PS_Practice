for tc in range(1, int(input())+1):
    MAX = 0
    MIN = 1000001
    n = int(input())
    nums = list(map(int, input().split()))
    for num in nums:
        if num < MIN:
            MIN = num
        if num > MAX:
            MAX = num
    print("#"+str(tc), MAX - MIN)
