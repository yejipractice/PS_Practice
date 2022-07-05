import sys
input = sys.stdin.readline
from collections import deque

n = int(input())

graph = [[0 for i in range(n)]for j in range(n)]

snake = deque()
snake.append((0, 0))

now_dir = 0 #오른쪽

dir = [0, 1, 2, 3] # 오른쪽, 아래, 왼쪽, 위 
l = [3, 0, 1, 2] # 왼
d = [1, 2, 3, 0] # 오른 


for i in range(int(input())):
    a, b = map(int, input().split())
    graph[a-1][b-1] = 1

steps = []
input_n = int(input())
for _ in range(input_n):
    x, c = map(str, input().split())
    x = int(x)
    steps.append((x, c))
    
def go(dir):
    first_x, first_y = snake.popleft()
    if dir == 0:
        first_dx, first_dy = first_x, first_y+1
    elif dir == 1:
        first_dx, first_dy = first_x+1, first_y
    elif dir == 2:
        first_dx, first_dy = first_x, first_y-1
    else:
        first_dx, first_dy = first_x-1, first_y
    if first_dx < 0 or first_dx >= n or first_dy < 0 or first_dy >= n or (first_dx, first_dy) in snake:
        return False
    if graph[first_dx][first_dy]==1:
        graph[first_dx][first_dy] = 0
        snake.appendleft((first_x, first_y))
        snake.appendleft((first_dx, first_dy))
    else:
        snake.appendleft((first_x, first_y))
        snake.appendleft((first_dx, first_dy))
        snake.pop()
    return True


time = 0
def game():
    global now_dir
    global time
    for x, c in steps:
        for t in range(time, x):
            time+=1
            res = go(now_dir)
            if res == False:
                return
        if c == "D":
            now_dir = d[now_dir]
        else:
            now_dir = l[now_dir]
    while 1:
        time+=1
        res = go(now_dir)
        if res == False:
            return
        

game()
print(time)