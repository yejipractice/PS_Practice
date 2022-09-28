N = int(input())

def moo(acc, cur, N):
    prev = (acc-cur)//2
    if N <= prev: return moo(prev, cur-1, N)
    elif N > prev+cur: return moo(prev, cur-1, N-prev-cur)
    else: return "o" if N-prev-1 else "m"

acc, n = 3, 0
while N > acc:
    n += 1
    acc = acc*2+n+3

print(moo(acc, n+3, N))

'''
Moo 수열을 다음과 같이 생각한다.

Moo(n) = Moo(n-1) + "m" + "o"*(n+2) + Moo(n-1)

여기서 Moo(n)를 양 옆의 Moo(n-1)부분과 가운데의 mooo...(o*(n+2)) 부분으로 나눌 수 있다.

이 때, N번째 문자는 왼쪽 Moo(n-1), 오른쪽 Moo(n-1), 그리고 가운데 부분 중 하나에 존재한다.

이 점을 응용하여 분할정복법으로 해결할 수 있다.

 

먼저 길이가 N번째 문자를 찾으려면 Moo(n)의 길이가 N이상이어야 하므로,

while문에서 이를 만족하는 n을 찾는다.

 

moo 함수에서는 Moo(n)의 길이, 가운데 부분의 길이, N이 매개변수로 주어진다.

Moo(n-1)의 길이는 Moo(n)의 길이에서 가운데 부분의 길이를 뺀 후 2로 나눈 것과 같다.

 

왼쪽 Moo(n-1)부분에 N이 존재하면 사실상 Moo(n-1)의 N번째 문자를 찾는 것과 같다.

오른쪽 Moo(n-1)부분에 N이 존재하면 Moo(n-1)의 (N-Moo(n-1)의길이-가운데부분길이)번째 문자를 찾는 것과 같다.

가운데 부분에 N이 존재한다면 바로 N번째 문자를 알 수 있다.

왜냐하면 가운데 부분은 한 개의 m과 (n+2)개의 o로 구성되어 있기 때문이다.

즉, N이 가운데 부분의 첫 번째라면 m이고 그렇지 않다면 o이다.
https://tesseractjh.tistory.com/101
'''