import sys
input = sys.stdin.readline

inputs = list(input().strip())

count = 0
lcount = 0
for i in range(len(inputs)):
    if inputs[i] == "(":
        if i != len(inputs) and inputs[i+1] == ")":
            inputs[i] = "0"
            inputs[i+1] = "0"
            count += lcount
        else:
            lcount += 1
    elif inputs[i] == ")":
        lcount -= 1
        count += 1

print(count)

# 레이저 기준 ( 개수
