import sys
input = sys.stdin.readline

N = int(input())
for _ in range(N):
    array = list(map(str, input().strip()))
    answer = "YES"
    while(True):
        if ")" not in array and "(" not in array:
            break
        if ")" in array and "(" not in array:
            answer = "NO"
            break
        if "(" in array and ")" not in array:
            answer = "NO"
            break
        a = array.index(")")
        b = array.index("(")
        if b < a:
            array[a] = 0
            array[b] = 0
        else:
            answer = "NO"
            break

    print(answer)
