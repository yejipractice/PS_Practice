from collections import deque  # 큐 구현
import sys
input = sys.stdin.readline

queue = deque()

N = int(input())

for _ in range(N):
    word = input().strip()
    if word == "size":
        print(len(queue))
    elif word == "empty":
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif word == "front":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
    elif word == "back":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])
    elif word == "pop":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.popleft())
    else:
        alpha = int(word[5:])
        queue.append(alpha)

# push 뒤에 입력되는 정수가 한자리가 아닐 수도 있음
