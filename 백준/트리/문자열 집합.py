n, m = map(int, input().split())

words = {}  # 시간 초과를 방지하기 위해 딕셔너리로 구현
for _ in range(n):
    words[input()] = True

cnt = 0
for _ in range(m):
    newWord = input()
    if words.get(newWord, False) == True:
        cnt += 1
print(cnt)

# 트리로 어떻게 풀까 .. .?
