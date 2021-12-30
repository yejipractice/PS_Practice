tc = int(input())

dic = {
    '0001101':'0',
    '0011001':'1',
    '0010011':'2',
    '0111101':'3',
    '0100011':'4',
    '0110001':'5',
    '0101111':'6',
    '0111011':'7',
    '0110111':'8',
    '0001011':'9',   
}

for t in range(1, tc+1):
    n, m = map(int, input().split())
    array = []
    checked = False
    for _ in range(n):
        arr = list(map(int, input()))
        if sum(arr) != 0 and checked==False:
            array = arr;
            checked = True
    array.reverse()
    first = array.index(1)
    real = array[first:first+56]
    real.reverse()
    ans = []
    for j in range(0, 56, 7):
        sub = []
        for idx in range(j, j+7):
            sub.append(str(real[idx]))
        sub = "".join(sub)
        ans.append(int(dic[sub]))
    odd = 0;
    even = 0;
    for k in range(len(ans)):
        index = k+1
        if index%2 == 0:
            even+=int(ans[k])
        else:
            odd+=int(ans[k])
    res = odd*3+even
    print("#"+str(t), end=" ");
    print(sum(ans) if res%10==0 else 0)
        
    