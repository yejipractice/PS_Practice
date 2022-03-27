import heapq

# 우선 순위 큐 순서 반대로 하기 위한 방법 (-1 곱해주기)
# 이중우선순위큐는 아래와 같이


def solution(operations):
    max_arr = []
    min_arr = []
    for operarion in operations:
        op, num = map(str, operarion.split())
        num = int(num)
        if op == "I":
            heapq.heappush(max_arr, num)
            heapq.heappush(min_arr, -1*num)
        else:
            if len(max_arr) == 0:
                continue
            if num == 1:
                cur = heapq.heappop(min_arr)
                max_arr.remove(-1*cur)
            else:
                cur = heapq.heappop(max_arr)
                min_arr.remove(-1*cur)
    if len(max_arr) == 0:
        return [0, 0]
    minans = min(max_arr)
    maxans = max(max_arr)
    return [maxans, minans]


arr = ["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]
answer = solution(arr)
print(answer)
