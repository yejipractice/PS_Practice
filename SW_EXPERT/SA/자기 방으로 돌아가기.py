
for tc in range(1, int(input())+1):
    n = int(input())
    visited = [0 for i in range(401)]
    for _ in range(n):
        a, b = map(int, input().split())

        # 학생들의 방 위치를 복도를 기준으로 바꾸어서 카운팅
        #  stu_room 1 3 5 7 ... 399
        #  corridor 0 1 2 3 ... 199
        #  stu_room 2 4 6 8 ... 400
        #  겹치는 복도 카운트

        if a <= b:
            start = (a-1)//2
            end = (b-1)//2
        else:
            start = (b-1)//2
            end = (a-1)//2
        for idx in range(start, end+1):
            visited[idx] += 1
    print("#"+str(tc)+" "+str(max(visited)))
