import sys
import collections
input = sys.stdin.readline

N = int(input())

nums = []
for _ in range(N):
    nums.append(int(input()))

nums.sort()
avg = round(sum(nums)/N)
center = nums[int((1+N)/2)-1]
ranges = nums[-1]-nums[0]
# Counter 와 Dictionary 사용법
most_dic = collections.Counter(nums).most_common()
if len(nums) == 1:
    most = nums[0]
elif most_dic[0][1] == most_dic[1][1]:
    most = most_dic[1][0]
else:
    most = most_dic[0][0]


print(avg)
print(center)
print(most)
print(ranges)
