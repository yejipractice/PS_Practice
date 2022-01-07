for tc in range(1, int(input())+1):
    answer = 0
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a.sort()
    for bb in b:
        start = 0
        end = len(a)-1
        history = 0
        while start <= end:
            mid = (start+end)//2
            if bb == a[mid]: #  # 연속 같은 방향이 발생하지 않았으면서 값 존재 => 조건 성립
                answer +=1
                break
            if bb>= a[mid]:
                if history == 1: # 연속 같은 방향 
                    break
                else:
                    start = mid+1
                    history = 1
            else:
                if history == 2:  # 연속 같은 방향
                    break;
                else:
                    end = mid-1
                    history = 2
    print(answer)
            

'''
입력
3
3 3
1 2 3
2 3 4
3 5
1 3 5
2 4 6 8 10
5 5
1 3 5 7 9
1 2 3 4 5
출력
#1 2
#2 0
#3 3
'''