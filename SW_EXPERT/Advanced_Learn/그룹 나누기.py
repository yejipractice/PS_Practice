def Find_Set(x):
    if parents[x] == x:
        return x
    return Find_Set(parents[x])


def Union_Set(x, y):
    parents[Find_Set(y)] = Find_Set(x)


for tc in range(1, int(input())+1):
    n, m = map(int, input().split())
    parents = [i for i in range(0, n+1)]
    inputs = list(map(int, input().split()))
    for idx in range(0, len(inputs), 2):
        x, y = inputs[idx], inputs[idx+1]
        Union_Set(x, y)
    result = set()
    for mem in range(1, n+1):
        result.add(Find_Set(mem))
    print("#"+str(tc)+" "+str(len(result)))
