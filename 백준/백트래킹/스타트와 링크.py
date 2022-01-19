n = int(input())
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))
min_team = 100*21
selected = [0]*(n+1)


def dfs(start, selected):
    global min_team
    if sum(selected) == n//2:
        sum_team = 0
        another = 0
        for i in range(1, n+1):
            for j in range(1, n+1):
                if i != j:
                    if selected[i] == 1 and selected[j] == 1:
                        sum_team += board[i-1][j-1]
                    elif selected[i] == 0 and selected[j] == 0:
                        another += board[i-1][j-1]
        min_team = min(abs(another-sum_team), min_team)
    for i in range(start, n+1):
        if selected[i] == 0:
            selected[i] = 1
            dfs(i+1, selected)
            selected[i] = 0


dfs(1, selected)  # start 인자를 넣어줌으로써 1,4 & 4,1 중복 계산 방지

print(min_team)

# 완전검색을 해야했다. 그래도 itertools보다 빠르다.
