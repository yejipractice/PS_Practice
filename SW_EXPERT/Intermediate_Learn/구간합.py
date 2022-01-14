for tc in range(1, int(input())+1):
    n, m = map(int, input().split())
    nums = list(map(int, input().split()))
    maxSum = -1
    minSum = 10000*m+1
    for i in range(0, n-m+1):
        s = sum(nums[i:i+m])
        maxSum = max(s, maxSum)
        minSum = min(s, minSum)
    print("#"+str(tc), maxSum-minSum)
