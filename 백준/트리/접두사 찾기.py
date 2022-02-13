n, m = map(int, input().split())

words = []
for _ in range(n):
    words.append(input())

cnt = 0
for _ in range(m):
    newWord = input()
    for word in words:
        w = word[:len(newWord)]
        if w == newWord:
            cnt += 1
            break
print(cnt)

# 트리로 어떻게 풀까 .. .?
