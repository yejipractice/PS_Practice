def Find_Set(x):
    if parents[x] != x:
        parents[x] = Find_Set(parents[x])
    return parents[x]


def Union_Set(x, y):
    Link(Find_Set(x), Find_Set(y))


def Link(x, y):
    if rank[x] > rank[y]:
        parents[y] = x
    else:
        parents[x] = y
    if rank[x] == rank[y]:
        rank[y] += 1


for tc in range(1, int(input())+1):
    n, m = map(int, input().split())
    parents = [i for i in range(0, n+1)]
    rank = [0 for i in range(0, n+1)]
    inputs = list(map(int, input().split()))
    for idx in range(0, len(inputs), 2):
        x, y = inputs[idx], inputs[idx+1]
        Union_Set(x, y)
    result = set()
    for mem in range(1, n+1):
        # Find_Set 실행하면서 상위 노드를 저장하기 때문에 모두 Find_Set 해줘야 한다.
        result.add(Find_Set(mem))
    print("#"+str(tc)+" "+str(len(result)))
