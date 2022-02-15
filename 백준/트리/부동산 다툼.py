import sys
input = sys.stdin.readline  # 입출력 라이브러리 꼭 써주기

n, q = map(int, input().split())
visited = set()
for _ in range(q):
    now = int(input())
    origin = now
    already = 0
    while now > 1:
        if now in visited:
            # 아래부터 순회하며 올라가는데 처음 경유한 노드를 마주치는 경우를 찾아야 하므로 break 넣으면 안된다.
            already = now
        now //= 2
    print(already)
    if already == 0:
        visited.add(origin)
