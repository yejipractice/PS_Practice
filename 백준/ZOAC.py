import sys
input = sys.stdin.readline

word = list(input().rstrip())

now = ""
now_idx = -1
visited = list(0 for i in range(len(word)))

def find(pre, pre_word):
    if pre == -1:
        result, result_idx = word[0], 0
        for idx in range(1, len(word)):
            if word[idx] < result:
                result, result_idx = word[idx], idx        
        return result, result_idx
    else:
        result, result_idx = "", -1
        for idx in range(len(word)):
            if visited[idx] == 1:
                continue
            if idx < pre:
                next = word[idx]+pre_word
            else:
                next = pre_word+word[idx]
            if result == "":
                    result, result_idx = next, idx
            else:
                if next < result:
                    result, result_idx = next, idx
        return result, result_idx

for step in range(len(word)):
    if step == 0:
        now, now_idx = find(-1, "")
        visited[now_idx] = 1
        print(now)
    else:
        now, now_idx = find(now_idx, now)
        visited[now_idx] = 1
        print(now)
    


