import sys
input = sys.stdin.readline

n, l = map(int, input().split())
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))


def check(line):
    checked = [False for i in range(n)]  # 경사로 사용 여부 체크
    for i in range(n - 1):
        if line[i] == line[i + 1]:
            continue
        if abs(line[i] - line[i + 1]) > 1:  # 1 이상 나면 안됨
            return False
        if line[i] > line[i + 1]:  # 경사로 사용 가능 여부 위한 범위 체크
            temp = line[i + 1]    # 경사로 범위 동안 값이 동일 해야 하며
            for j in range(i + 1, i + 1 + l):  # 이미 경사로를 사용중인 위치면 안됨
                if 0 <= j < n:
                    if line[j] != temp:
                        return False
                    if checked[j] == True:
                        return False
                    checked[j] = True
                else:
                    return False
        else:
            temp = line[i]
            for j in range(i, i - l, -1):
                if 0 <= j < n:
                    if line[j] != temp:
                        return False
                    if checked[j] == True:
                        return False
                    checked[j] = True
                else:
                    return False
    return True


cnt = 0
for i in board:
    if check(i):
        cnt += 1

for i in range(n):  # 세로
    temp = []
    for j in range(n):
        temp.append(board[j][i])
    if check(temp):
        cnt += 1

print(cnt)
