from inspect import stack
import sys
input = sys.stdin.readline

# n = int(input())
# array = []
# for _ in range(n):
#     array.append(int(input()))

# cnt = 0
# while True:
#     minn = min(array)
#     maxx = max(array)
#     if minn == maxx:
#         break
#     idx = array.index(minn)
#     left, right = idx-1, idx+1
#     if 0<=left < len(array) and array[left]==minn:
#         array[left]+=1
#     if 0<=right < len(array) and array[right]==minn:
#         array[right]+=1
#     array[idx]+=1
#     cnt+=1
    
# print(cnt)

# 이걸 어떻게 생각해내지 .. ? 

n = int(input())
stack = []
cnt = 0
m = 0
for _ in range(n):
    x = int(input())
    m = max(m, x)
    if stack:
        if stack[-1] < x:
            cnt+=x-stack.pop()
            stack.append(x)
        else:
            stack.pop()
            stack.append(x)
    else:
        stack.append(x)
        
while stack:
    cnt+=m-stack.pop()
    
print(cnt) 
