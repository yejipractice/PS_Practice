x, y, w, h = map(int, input().split())

distances = [x, y, h-y, w-x]
print(min(distances))
