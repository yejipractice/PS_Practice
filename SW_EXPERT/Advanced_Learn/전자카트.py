
from itertools import permutations

tc = int(input())
for t in range(1, tc+1):
    n = int(input())
    board = []
    answer = 100*(n**n);
    for _ in range(n):
        board.append(list(map(int, input().split())))
    cases = list(permutations([x for x in range(2, n+1)]))
    for case in cases:
        pre = 1
        sum = 0 
        for i in range(len(case)):
            next = case[i]
            sum+=board[pre-1][next-1]
            pre = next
        sum += board[pre-1][0];
        answer = min(answer, sum)
    print("#"+str(t), end=" ")
    print(answer)