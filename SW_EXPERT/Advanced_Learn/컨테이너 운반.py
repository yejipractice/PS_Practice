tc = int(input())
for tt in range(1, tc+1):
    n, m = map(int, input().split())
    w = list(map(int, input().split()))
    t = list(map(int, input().split()))
    w.sort()
    t.sort()
    answer = 0
    while w and t: # 런타임에러 조심 
        truck = t.pop()
        while w:
            gift = w.pop()
            if gift <= truck:
                answer += gift
                break
    print("#"+str(tt), end=" ")
    print(answer)

    
'''
입력    
3
3 2
1 5 3
8 3
5 10
2 12 13 11 18
17 4 7 20 3 9 7 9 20 5
10 12
10 13 14 6 19 11 5 20 11 14
5 18 17 8 9 17 18 4 1 16 15 13

출력
#1 8
#2 45
#3 84
'''