tc = int(input())
for t in range(1, tc+1):
    answer = []
    n = int(input())
    inputs = list(map(int, input().split()))
    xs = inputs[:n]
    ms = inputs[n:]
    for i in range(n-1):
        x1, x2 = xs[i], xs[i+1]
        m1, m2 = ms[i], ms[i+1]
        m11 = m1**(1/2)
        m22 = m2**(1/2)
        p = round(m11/(m11+m22),10)
        ans = x1+(p)*(x2-x1)
        answer.append(round(ans, 10))
    print("#"+str(t), end=" ")
    for tt in range(len(answer)):
        print(format(answer[tt],".10f"), end=" ")  
    print()
