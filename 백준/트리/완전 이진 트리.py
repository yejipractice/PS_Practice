import sys
input = sys.stdin.readline

k = int(input())
tree = [[] for i in range(k+1)]
inputs = list(map(int, input().split()))


def make_tree(level, sub_tree):
    mid = len(sub_tree)//2
    tree[level].append(sub_tree[mid])
    if len(sub_tree) == 1:
        return
    make_tree(level+1, sub_tree[:mid])
    make_tree(level+1, sub_tree[mid+1:])


make_tree(1, inputs)
for lev in range(1, k+1):
    if tree[lev] != []:
        print(*tree[lev])
