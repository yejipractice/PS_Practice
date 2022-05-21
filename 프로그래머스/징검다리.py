def solution(distance, rocks, n):
    answer = 0
    start, end = 0, distance
    
    rocks.sort() #정렬되어 있지 않은 상태이기 때문에 정렬해야한다.
    
    while start <= end:
        mid = (start+end)//2 # 중간 값
        del_stones = 0 # 제거된 돌 개수 
        pre_stone = 0 # 기준
        for rock in rocks:
            if rock - pre_stone < mid:
                del_stones+=1
            else:
                pre_stone = rock
            if del_stones > n:
                break
        if del_stones > n:
            end = mid -1
        else:
            answer = mid
            start = mid+1
    return answer

r = [2, 14, 11, 21, 17]
print(solution(25, r, 2))



# 시간 초과 
# from itertools import combinations
# import copy

# def solution(distance, rocks, n):
#     answer = []
#     for array in combinations(rocks, n):
#         result = []
#         rock = copy.deepcopy(rocks)
#         rock.append(25)
#         rock.append(0)
#         for ar in array:
#             rock.pop(rock.index(ar))
#         rock.sort()
#         for idx in range(1, len(rock)):
#             result.append(rock[idx]-rock[idx-1])
#         answer.append(min(result))
#     return max(answer)


