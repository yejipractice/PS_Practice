rep = int(input())


def function(H, W, N):
    # N이 H로 나눠어 떨어지는가를 기준으로!
    w = (N // H + 1)if N % H != 0 else N // H
    h = N - H * (w-1)
    result = str(h)+"0"+str(w) if w < 10 else str(h)+str(w)
    print(result)


for i in range(rep):
    H, W, N = map(int, input().split())
    function(H, W, N)
