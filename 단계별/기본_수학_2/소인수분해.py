n = int(input())

while n != 1:
    for i in range(2, n+1):
        if n % i == 0:
            print(i)
            n = n//i
            break

# /연산을 하게 되면 결과값은 float으로 나오기 때문에 //연산자를 통해 자연수인 몫만 구한다.
