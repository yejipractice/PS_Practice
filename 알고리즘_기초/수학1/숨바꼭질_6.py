import math
import sys
input = sys.stdin.readline
N, S = map(int, input().split())
visits = list(map(int, input().split()))
distances = list(set([abs(visit-S) for visit in visits]))
dis = min(distances)
for d in distances:
    dis = math.gcd(d, dis)

print(dis)
