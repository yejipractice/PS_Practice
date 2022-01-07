def merge(left, right):
    global answer
    array = []
    
    if left[-1] > right[-1]:
        answer+=1
    
    n = len(left)
    m = len(right)
    
    lidx, ridx = 0,0;
    
    while lidx != n and ridx != m:
        if left[lidx] <= right[ridx]:
            array.append(left[lidx])
            lidx+=1
        else:
            array.append(right[ridx])
            ridx+=1
        
    if lidx != n:
        array+=left[lidx:]
    if ridx != m:
        array+=right[ridx:]
    return array

def merge_sort(list):
    if len(list) <=1:
        return list;
    
    mid = len(list)//2
    left = merge_sort(list[:mid])
    right = merge_sort(list[mid:])
    
    return merge(left, right)

for tc in range(1, int(input())+1):
    n = int(input())
    nums = list(map(int, input().split()))
    answer = 0
    merged = merge_sort(nums)
    result = merged[len(merged)//2]
    print("#"+str(tc), end=" ")
    print(result, answer)
   
   
# linkedlist로 했을 때 시간 초과가 났다. 인덱스로 접근하는 것이 더 빨라서 그런가보다.  
'''
입력
2
5
2 2 1 1 3
10
7 5 4 1 2 10 3 6 9 8
출력
#1 2 0
#2 6 6
'''