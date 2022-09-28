import heapq

n, k = map(int, input().split())

jews = []
bags = []

for _ in range(n):
    heapq.heappush(jews, list(map(int, input().split())))

for _ in range(k):
    bags.append(int(input()))
bags.sort()

answer = 0
temp = []

# 최소힙, 최대힙 사용하여 구현, temp를 이용해서 그리디: 사용가능한 후보 모두 구해놓은 다음 그때마다 최선  
for bag in bags:
    while jews and bag >= jews[0][0]:
        heapq.heappush(temp, -heapq.heappop(jews)[1])
    if temp:
        answer += -heapq.heappop(temp)
    elif not jews:
        break

print(answer)
        
# python3으로 시간초과, pypy3으로 통과