tt = int(input())
for tc in range(1, tt+1):
    n = int(input())
    times = []
    for _ in range(n):
        start, end = map(int, input().split())
        times.append([start, end])
    times.sort(key=lambda x: x[1], reverse=True)
    answer = 0
    pre_end = 0;
    while times:
        s, e = times.pop()
        if s >= pre_end:
            answer +=1
            pre_end = e
    print("#"+str(tc), end=" ")
    print(answer)
    
'''
입력
3
5
20 23
17 20
23 24
4 14
8 18
10
14 23
2 19
1 22
12 24
21 23
6 15
20 24
1 4
6 15
15 16
15
18 19
2 7
11 15
13 16
23 24
2 14
13 22
20 23
13 19
7 15
5 21
20 24
16 22
17 21
9 24
출력
#1 4
#2 4
#3 5
'''