from collections import deque
# 큐 사용할 때에는 deque 라이브러리 사용하기 list사용하면 시간 초과

Max_num = 1000000

for tc in range(1, int(input())+1):
    n, m = map(int, input().split())
    queue = deque()
    visited = {}  # 이 경우에는 리스트보다 딕셔너리가 빨랐음
    answer = Max_num
    queue.append((n, 0))
    while queue:
        sum, count = queue.popleft()
        if visited.get(sum, 0):  # default 값 0
            continue
        visited[sum] = 1
        if sum == m:
            answer = min(count, answer)
            break
        if 0 < sum+1 <= Max_num:
            queue.append((sum+1, count+1))
        if 0 < sum-1 <= Max_num:
            queue.append((sum-1, count+1))
        if 0 < sum*2 <= Max_num:
            queue.append((sum*2, count+1))
        if 0 < sum-10 <= Max_num:
            queue.append((sum-10, count+1))
    print("#"+str(tc)+" "+str(answer))
