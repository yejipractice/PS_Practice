import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n = int(input())
    stickers = []
    for __ in range(2):
        stickers.append(list(map(int, input().split())))

    # 인덱스 에러 고려
    if n > 1:
        stickers[0][1] += stickers[1][0]
        stickers[1][1] += stickers[0][0]
        for i in range(2, n):
            stickers[0][i] = max(stickers[1][i-1]+stickers[0][i],
                                 stickers[0][i]+max(stickers[0][i-2], stickers[1][i-2]))
            stickers[1][i] = max(stickers[0][i-1]+stickers[1][i],
                                 stickers[1][i]+max(stickers[0][i-2], stickers[1][i-2]))

    print(max(stickers[0][n-1], stickers[1][n-1]))
