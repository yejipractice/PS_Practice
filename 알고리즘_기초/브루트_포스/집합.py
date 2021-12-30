import sys
input = sys.stdin.readline

array = set()
n = int(input())

for _ in range(n):
    inp = input().rstrip().rsplit()
    if len(inp) == 1:
        if inp[0] == "all":
            array = set([i for i in range(1, 21)])
        elif inp[0] == "empty":
            array = set()
    else:
        op, num = inp[0], int(inp[1])
        if op == "add":
            array.add(num)
        elif op == "remove":
            array.discard(num)
        elif op == "check":
            if num in array:
                print(1)
            else:
                print(0)
        elif op == "toggle":
            if num in array:
                array.discard(num)
            else:
                array.add(num)

# array가 아니라 set을 이용하면 더 간단하게 구현 가능
