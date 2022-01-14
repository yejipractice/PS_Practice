n = int(input())
count = 0
memo = [0 for _ in range(n+1)]


def check(v):
    for i in range(1, v):
        if memo[v] == memo[i] or (abs(memo[v] - memo[i]) == abs(v-i)):
            return False
    return True


def dfs(v):
    global count
    if not check(v):
        return
    if v == n:
        count += 1
        return
    for i in range(1, n+1):
        memo[v+1] = i
        dfs(v+1)


dfs(0)

print(count)

# 시간 초과
