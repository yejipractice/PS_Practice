tc = int(input())
for t in range(1, tc+1):
    n = int(input())
    line = list(map(int, input().split()))
    x = line[:n]
    m = line[n:]
    ans = []
    for i in range(1, n):
        low = x[i-1]
        high = x[i]
        while high - low > 1/(10**12):
            mid = (low+high) /2
            left = right = 0
            for i in range(n):
                force = m[i] / (mid-x[i])**2
                if x[i] < mid:
                    left+=force
                else:
                    right += force
            if left < right:
                high = mid
            else:
                low = mid
        ans.append(mid)
    print('#%s %s' % (tc, ' '.join('%.10f' % f for f in ans)))
    
    # 문제 이해 부족 -> 이분탐식 응용법만 익히고 넘어감 