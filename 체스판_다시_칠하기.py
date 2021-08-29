first = list(map(str, "BWBWBWBW"))
second = list(map(str, "WBWBWBWB"))

types = [[], []]

for _ in range(4):
    types[0].append(first)
    types[0].append(second)
    types[1].append(second)
    types[1].append(first)

N, M = map(int, input().split())

all = []
cases = []

for i in range(N):
    all.append(list(map(str, input())))

for i in range(0, M-8+1):
    for j in range(0, N-8+1):
        alist = []
        for jj in range(j, j+8):
            alist.append(all[jj][i:i+8])
        cases.append(alist)

ans = 8*8
for case in cases:
    for type in types:
        count = 0
        for i in range(0, 8):
            for j in range(0, 8):
                if case[i][j] != type[i][j]:
                    count += 1
        ans = min(ans, count)

print(ans)
