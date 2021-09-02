strs = list(map(str, input()))

answer = []
container = []
switch = 0
for i in range(len(strs)):
    if strs[i] == "<":
        answer.append("".join(list(reversed(container))))
        container = []
        switch = 1
        container.append(strs[i])
    elif strs[i] == ">":
        switch = 0
        container.append(strs[i])
        answer.append("".join(container))
        container = []
    elif strs[i] == " ":
        if switch == 1:
            container.append(strs[i])
        else:
            answer.append("".join(list(reversed(container))))
            answer.append(" ")
            container = []
    elif i == len(strs)-1:
        container.append(strs[i])
        answer.append("".join(list(reversed(container))))
    else:
        container.append(strs[i])

print("".join(answer))
