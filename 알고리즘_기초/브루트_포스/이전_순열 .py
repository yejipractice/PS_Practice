import sys
input = sys.stdin.readline

n = int(input())
s = list(map(int, input().split()))

k = -1
for i in range(len(s)-1):
    if s[i] > s[i+1]:
        k = i

if k == -1:
    print(-1)
else:
    for j in range(k+1, len(s)):
        if s[j] < s[k]:
            m = j
    s[k], s[m] = s[m], s[k]

    temp = s[k+1:]
    temp.sort(reverse=True)
    answer = s[:k+1] + temp

    print(*answer)


# 파이썬 prev_permutation 알고리즘
# 1. array[k] > array [k+1] 가 성립하는 k의 최댓값을 찾는다
#    (만약 여기서 k값이 존재하지 않는다면 이미 오름차순으로 정렬되어 있다는 뜻)
# 2. 인덱스 k 이후의 값들 중 array[k] > array[m]이 성립하는 m의 최댓값을 찾는다.
# 3. k와 m의 자리의 값을 서로 바꾸어 준다.
# 4. 인덱스 k 이후의 값들을 내림차순으로 정렬해준다.
