
tc = int(input())

for i in range(1, tc+1):
    isov = False
    n = float(input())
    ans = []
    while(1): # 실수 2진수로 변환
        n = n*2
        ans.append(int(n//1))
        if n%1==0:
            break;
        if len(ans) >= 13:
            isov=True
        n-=n//1
    print("#"+str(i),end=" ")
    print("".join(map(str, ans)) if not isov else "overflow")
        
    

'''
입력
3
0.625
0.1
0.125

출력
#1 101
#2 overflow
#3 001	 
'''