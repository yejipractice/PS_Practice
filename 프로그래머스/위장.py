def solution(clothes):
    box = {}
    for cl in clothes:
        whe = cl[1]
        if box.get(whe, False) == False:
            box[whe] = 1
        else:
            box[whe] += 1
    answer = 1
    for v in box.values():
        print(v)
        answer *= (v+1)
    return answer-1


ans = solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"],
                ["green_turban", "headgear"]])
print(ans)
