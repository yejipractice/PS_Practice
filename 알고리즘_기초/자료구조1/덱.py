from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
queue = deque()

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
    elif "push_front" in word:
        alpha = word[11:]
        queue.appendleft(alpha)
    elif "push_back" in word:
        alpha = word[10:]
        queue.append(alpha)
    elif "pop_front" in word:
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.popleft())
    elif "pop_back" in word:
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.pop())
