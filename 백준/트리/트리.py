import sys
input = sys.stdin.readline

n = int(input())
tree = list(map(int, input().split()))
k = int(input())


def dfs(node, tree):
    tree[node] = -2
    for idx in range(n):
        if tree[idx] == node:
            dfs(idx, tree)


dfs(k, tree)
cnt = 0
for node in range(n):
    if tree[node] != -2 and node not in tree:
        cnt += 1
print(cnt)


#  dfs함수

#   전달받은 인덱스의 배열 값을 삭제한다는 의미로 -2로 바꾼다. (-1은 루트노드와 겹치므로 피한다.)

#   배열 전체를 탐색하며, 방금 삭제한 인덱스를 부모노드로 가지는 노드를 찾아 dfs함수를 재귀호출한다.

#   재귀가 끝나면 삭제될 노드들은 전부 -2로 갱신되어있으므로,

#   -2가 아니면서, 다른 노드의 부모노드도 아닌 원소를 찾을 때마다 count를 1씩 늘린다.
