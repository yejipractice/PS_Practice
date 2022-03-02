import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

pre_order = []
post_order = []

while True:
    try:
        pre_order.append(int(input()))
    except:
        break


def post_order_set(preorder, left, right):
    if left > right:
        return
    root = preorder[left]
    ls = left + 1
    rs = right+1
    re = right
    for i in range(right-left+1):
        if i == 0:
            continue
        if preorder[left+i] > root:
            rs = i+left
            break
    le = rs - 1
    post_order_set(pre_order, ls, le)
    post_order_set(pre_order, rs, re)
    post_order.append(root)


post_order_set(pre_order, 0, len(pre_order)-1)

for p in post_order:
    print(p)
