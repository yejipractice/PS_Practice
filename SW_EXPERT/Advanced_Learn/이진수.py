import sys
input = sys.stdin.readline

tc = int(input())

# 16진수 한자리씩 2진수로 변환 

def binary(n): # 10 -> 2
    ans = []
    while(n>0):
        a = n%2
        n = n//2
        ans.append(a)
    while(len(ans)<4):
        ans.append(0)
    ans.reverse();
    return ans;

for i in range(1, tc+1):
    n, six = map(str, input().split())
    n = int(n)
    ans = []
    for j in range(n):
        num = int(six[j], 16) # 16진수 -> 10진수 
        ans.extend(binary(num))
    print("#"+str(i), end=" ")
    print("".join(map(str, ans)))
    

'''
입력
3
4 47FE
5 79E12
8 41DA16CD

출력
#1 0100011111111110
#2 01111001111000010010
#3 01000001110110100001011011001101	 
'''