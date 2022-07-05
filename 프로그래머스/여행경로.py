import sys
input = sys.stdin.readline
from collections import defaultdict
from collections import deque



def solution(tickets):
    answer = []
    box = defaultdict(list)
    for a, b in tickets:
        box[a].append(b)
    for k in box.keys():
        box[k].sort(reverse=True) 
        
    def DFS():
        stack = ["ICN"]
        while stack:
            start = stack[-1]
            if not box[start]:
                answer.append(stack.pop())
            else:
                stack.append(box[start].pop())
    DFS()
    return answer[::-1] # 역순으로 반환 
    
res =  solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]])
print(res)

# DFS의 순서를 스택에 저장했다가 스택 top에서 갈 수 있는 경로가 없을 경우에 answer에 추가합니다. 갈 수 있는 경로가 없다는 것은 그 공항이 제일 마지막 방문지라는 의미
# https://mjmjmj98.tistory.com/103