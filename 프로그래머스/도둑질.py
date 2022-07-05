import sys
input = sys.stdin.readline

def solution(money):
    dp = [0] * len(money)
    dp[0] = money[0]
    dp[1] = money[0]
    for idx in range(2, len(money)-1): # 첫번째 집 무조건 yes, 마지막 집 무조건 no
        dp[idx] = max(dp[idx-1], dp[idx-2]+money[idx])
    dpp = [0] * len(money)
    dpp[0] = 0
    dpp[1] = money[1]
    for idx in range(2, len(money)): # 첫번째 집 무조건 no
        dpp[idx] = max(dpp[idx-1], dpp[idx-2]+money[idx])
    return max(max(dp), max(dpp))
    

res = solution([1, 2, 3, 1])
print(res)