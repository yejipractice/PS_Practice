def solution(genres, plays):
    total = {}
    dic = set()
    for idx in range(len(genres)):
        g = genres[idx]
        if g not in total:
            total[g] = plays[idx]
        else:
            total[g] += plays[idx]
        dic.add((g, plays[idx], idx))
    totals = []
    kk = list(total.keys())
    vv = list(total.values())
    for t in range(len(total)):
        totals.append((kk[t], vv[t]))
    totals.sort(key=lambda x: x[1], reverse=True)
    answer = []
    for t1, t2 in totals:
        ans = []
        for d in dic:
            if d[0] == t1:
                ans.append((d[1], d[2]))
        ans.sort(reverse=True, key=lambda x: x[0])
        idxs = [a[1] for a in ans]
        if len(idxs) >= 2:
            answer.extend(idxs[:2])
        else:
            answer.extend(idxs[:1])
    return answer


ans = solution(["a", "b", "c", "d", "a", "d", "d", "d", "a", "a", "c", "c"],
               [100, 300, 400, 150, 100, 300, 200, 600, 700, 110, 900, 9000])
print(ans)
