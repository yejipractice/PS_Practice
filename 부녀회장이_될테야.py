rep = int(input())


for _ in range(rep):
    k = int(input())
    n = int(input())
    first = [i for i in range(1, n+1)]
    for a in range(k):
        for i in range(1, n):
            first[i] += first[i-1]
    print(first[-1])
