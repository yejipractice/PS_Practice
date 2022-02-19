def solution(participant, completion):
    answer = {}
    for part in participant:
        if answer.get(part, False) == False:
            answer[part] = 1
        else:
            answer[part] += 1
    for comp in completion:
        if answer.get(comp) == 1:
            answer.pop(comp)
        else:
            answer[comp] -= 1
    return list(answer.keys())


ans = solution(["leo", "kiki", "eden"], ["eden", "kiki"])
print(*ans)

# def solution(participant, completion):
#     answer = ''
#     temp = 0
#     dic = {}
#     for part in participant:
#         dic[hash(part)] = part
#         temp += int(hash(part))
#     for com in completion:
#         temp -= hash(com)
#     answer = dic[temp]

#     return answer

# import collections


# def solution(participant, completion):
#     answer = collections.Counter(participant) - collections.Counter(completion)
#     return list(answer.keys())[0]
