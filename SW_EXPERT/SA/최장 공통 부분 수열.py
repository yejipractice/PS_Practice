for tc in range(1, int(input())+1):
    word1, word2 = map(str, input().split())
    dp = [[0 for j in range(len(word2)+1)] for i in range(len(word1)+1)]

    for i in range(1, len(word1)+1):
        for j in range(1, len(word2)+1):
            if word1[i-1] == word2[j-1]:
                dp[i][j] = dp[i-1][j-1]+1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    print("#"+str(tc)+" "+str(dp[-1][-1]))
