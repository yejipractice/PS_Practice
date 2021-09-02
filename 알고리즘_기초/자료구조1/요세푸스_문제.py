from collections import deque

N, K = map(int, input().split())

nums = [i for i in range(1, N+1)]
queue = deque(nums)
prints = []

while(True):
    if len(queue) == 0:
        break
    for _ in range(K-1):
        pop_num = queue.popleft()
        queue.append(pop_num)
    print_pop = queue.popleft()
    prints.append(print_pop)

print("<", end="")
for i in range(len(prints)):
    if i == len(prints)-1:
        print(prints[i], end="")
    else:
        print(prints[i], end=", ")
print(">", end="")
