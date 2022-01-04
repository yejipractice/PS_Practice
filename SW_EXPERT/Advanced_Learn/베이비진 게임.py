tt = int(input())

def check(list):
    if 3 in list:
        return True
    for i in range(2, len(list)):
        if list[i-2]>=1 and list[i-1] >=1 and list[i] >=1:
            return True
    return False

for tc in range(1, tt+1):
    line = list(map(int, input().split()))
    one = [0 for x in range(10)]
    two = [0 for x in range(10)]
    ans = 0
    isOne = True
    for l in line:
        if isOne:
            one[l]+=1
            isOne = False
            if check(one) == True:
                ans = 1
                break
        else:
            two[l]+=1
            isOne = True
            if check(two) == True:
                ans = 2
                break
    print("#"+str(tc), end=" ")
    print(ans)
        
'''
입력
3
9 9 5 6 5 6 1 1 4 2 2 1
5 3 2 9 1 5 2 0 9 2 0 0
2 8 7 7 0 2 2 2 5 4 0 3
출력
#1 0
#2 1
#3 2
'''