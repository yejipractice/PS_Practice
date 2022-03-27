import heapq


def solution(jobs):
    seq = []
    sum, cnt, now = 0, 0, 0
    start = -1

    while cnt < len(jobs):
        for job in jobs:
            if start < job[0] <= now:
                heapq.heappush(seq, [job[1], job[0]])

        if 0 < len(seq):
            curr_time, curr_start = heapq.heappop(seq)
            start = now  # 이번 작업은 다음 가능 작업 목록에서 제외하기 위해
            now += curr_time
            sum += now - curr_start
            cnt += 1
        else:
            now += 1

    return sum // len(jobs)


arr = [[0, 3], [1, 9], [2, 6]]
answer = solution(arr)
print(answer)
