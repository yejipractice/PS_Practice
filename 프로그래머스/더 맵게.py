import heapq


def solution(scoville, K):
    heapq.heapify(scoville)  # 배열을 바로 힙으로 만드는 법
    time = 0
    while scoville[0] < K:
        if len(scoville) >= 2:
            heapq.heappush(scoville, heapq.heappop(
                scoville)+heapq.heappop(scoville)*2)
            time += 1
        else:
            return -1
    return time


sc = [1, 2, 3, 9, 10, 12]
k = 7
answer = solution(sc, k)
print(answer)
