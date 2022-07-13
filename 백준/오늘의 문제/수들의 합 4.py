from collections import defaultdict
n, m = map(int, input().split())
arr = list(map(int, input().split()))

cnt = 0
dic = defaultdict(int)
for i in range(1, len(arr)):
    arr[i] += arr[i-1]
    
for i in range(len(arr)):
    if arr[i] ==m:
        cnt += 1
    cnt += dic[arr[i]-m]
    dic[arr[i]] += 1
print(cnt)

# 아 어렵다 .. .