for tc in range(1, int(input())+1):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a.sort()
    answer = 0
    for i in range(m):
        start = 0
        end = n-1
        
        tar = b[i]
        history = 0
        while start<=end:
            mid = (start+end)//2
            if tar == a[mid]:
                answer +=1
                break
            elif tar > a[mid]:
                if history == 2:
                    break
                else:
                    start = mid+1
                    history =2
            elif a[mid] > tar:
                if history == 1:
                    break;
                else:
                    end = mid -1
                    history = 1
    print("#{} {}".format(tc, answer))
        