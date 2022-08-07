import sys
input = sys.stdin.readline

N, M, L = map(int, input().split())
arr = [0]+list(map(int, input().split()))+[L]
arr.sort()

start, end = 1, L-1
result = 0
while start <= end:
    count = 0
    mid = (start+end) // 2
    for i in range(1, len(arr)):
        # 구간 거리가 mid보다 큰 구간 찾기
        if arr[i]-arr[i-1] > mid:
            # 나눈 만큼 휴게소를 설치 (현재 설치 돼있는 구역은 제외해야해서 -1)
            count += (arr[i]-arr[i-1]-1)//mid
    if count > M:
        start = mid+1
    else:
        end = mid-1
        result = mid
print(result)


#  - mid : 가장 멀리 떨어져 있는 휴게소 사이 거리
# - count : 설치해야 할 휴게소 개수
# - 설치해야 할 휴게소 개수가 M보다 크다면 mid는 더 길어야 한다.
# - 설치해야 할 휴게소 개수가 M보다 작다면 mid는 더 짧아야 한다. (조건 만족은 했으므로 result = mid)