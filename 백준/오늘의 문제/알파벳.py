import queue
import sys
from unittest import result
input = sys.stdin.readline

r, c = map(int, input().split())

board = []

for _ in range(r):
    board.append(list(map(str, input().rstrip())))
    
xx = [0, 0, 1, -1]
yy = [1, -1, 0, 0]

result = 0
queue = set()
queue.add((0, 0, str(board[0][0])))

while queue:
    now_x, now_y, visited = queue.pop()
    result = max(result, len(visited))
    for idx in range(4):
        dx, dy = now_x+xx[idx], now_y+yy[idx]
        if 0<=dx<r and 0<=dy<c and board[dx][dy] not in visited:
            queue.add((dx, dy, visited+board[dx][dy]))
    
print(result)

# deque로 했을 떄에는 메모리 초과, set으로 하면 통과 