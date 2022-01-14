for tc in range(1, int(input())+1):
    n = int(input())
    nums = list(map(int, input()))
    cardInt = -1
    cardCount = 0
    for num in nums:
        c = nums.count(num)
        if c >= cardCount and num > cardInt:
            cardCount = c
            cardInt = num
    print("#"+str(tc), cardInt, cardCount)
