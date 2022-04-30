def solution(progresses, speeds):
    answer = []
    while len(progresses) != 0:
        cnt = 0
        while len(progresses) != 0 and progresses[0] > 99:
            progresses.pop(0)
            speeds.pop(0)
            cnt += 1
        if cnt != 0:
            answer.append(cnt)
        for i in range(len(progresses)):
            progresses[i] += speeds[i]
    return answer


p, g = [40, 93, 30, 55, 60, 65], [60, 1, 30, 5, 10, 7]
answer = solution(p, g)
print(answer)
