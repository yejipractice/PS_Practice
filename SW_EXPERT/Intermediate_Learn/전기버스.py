for tc in range(1, int(input())+1):
    k, n, m = map(int, input().split())  # 충전 당 최대 거리, 도착 지점, 충전기 있는 정류장 수
    batteries = list(map(int, input().split()))
    now = 0
    count = 0
    noAnswer = False
    while 1:
        if now >= n or noAnswer == True:
            break
        for i in range(k, 0, -1):
            pos = now+i
            if pos >= n:
                now = pos
                break
            if pos in batteries:
                now = pos
                count += 1
                break
            if i == 1 and pos not in batteries:
                noAnswer = True
                count = 0
    print("#"+str(tc), count)
