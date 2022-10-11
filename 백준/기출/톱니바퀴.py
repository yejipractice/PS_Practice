from collections import deque

first = deque(list(map(int, input())))
second = deque(list(map(int, input())))
third = deque(list(map(int, input())))
fourth = deque(list(map(int, input())))

wheels = [0, first, second, third, fourth]

def turn_right(queue):
    last = queue.pop()
    queue.appendleft(last)
    return

def turn_left(queue):
    first = queue.popleft()
    queue.append(first)
    return

def spread_right(now, dir):
    wheel = wheels[now]
    left = wheel[6]
    right = wheel[2]
    if dir == -1:
        turn_left(wheel)
    else:
        turn_right(wheel)
    if now + 1 <= 4:
        if right != wheels[now+1][6]:
            spread_right(now+1, dir*(-1))
    return

def spread_left(now, dir):
    wheel = wheels[now]
    left = wheel[6]
    right = wheel[2]
    if dir == -1:
        turn_left(wheel)
    else:
        turn_right(wheel)
    if now - 1 > 0:
        if left != wheels[now-1][2]:
            spread_left(now-1, dir*(-1))
    return

for _ in range(int(input())):
    num, dir = map(int, input().split())
    left = wheels[num][6]
    right = wheels[num][2]
    if dir == -1:
        turn_left(wheels[num])
    else:
        turn_right(wheels[num])
    if num - 1 > 0:
        if wheels[num-1][2] != left:
            spread_left(num-1, dir*(-1))
    if num+1 <= 4:
        if wheels[num+1][6] != right:
            spread_right(num+1, dir*(-1))

answer = first[0]*1+second[0]*2+third[0]*4+fourth[0]*8

print(answer)
