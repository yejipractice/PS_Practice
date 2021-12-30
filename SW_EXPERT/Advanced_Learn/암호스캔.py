tc = int(input().strip())

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
    n, m = map(int, input().strip().split())
    res = []
    for _ in range(n):
        array = list(map(str, input()))
        mustZero = False
        word = []
        for i in array:
            if i == "0":
                if mustZero:
                    continue
                else:
                    res.append("".join(word))
                    word.clear()
            else:
                if mustZero:
                    word.append(i)
                    mustZero = False
                else:
                    word.append(i)
    answer = list(set(res))
    real = []
    for ans in answer:
        if len(ans)!=0:
            sub = []
            for an in ans:
                hx = bin(int(an, 16))[2:]
                hex = format(int(hx), '04')
                sub.append(hex)
            real.append(("".join(map(str, sub))))
    real_answer = [];
    for r in real:
        r = list(r)
        r.reverse()
        first = r.index('1')
        realarray = r[first:first+56]
        realarray.reverse()
        ans = []
        for j in range(0, 56, 7):
            sub = []
            for idx in range(j, j+7):
                sub.append(str(realarray[idx]))
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
        if res%10 ==0:
            real_answer.append(sum(ans))
    print("#"+str(t), end=" ");
    print(sum(real_answer))
        