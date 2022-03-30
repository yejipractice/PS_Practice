
def solution(array, commands):
    answer = []
    for i, j, k in commands:
        new_arr = array[i-1:j]
        new_arr.sort()
        answer.append(new_arr[k-1])
    return answer


arr = [1, 5, 2, 6, 3, 7, 4]
com = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
answer = solution(arr, com)
print(answer)
