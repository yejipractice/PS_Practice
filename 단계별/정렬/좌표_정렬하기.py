import sys
input = sys.stdin.readline

N = int(input())

list = []
for _ in range(N):
    a, b = map(int, input().split())
    list.append([a, b])

list.sort(key=lambda x: (x[0], x[1]))  # 정렬 람다로 키를 설정할 때 다음과 같이로도 가능

for i in list:
    print(i[0], i[1])
