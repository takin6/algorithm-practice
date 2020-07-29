from collections import defaultdict

N = int(input())
nums = list(map(int, input().split()))

counter = defaultdict(list)
for i in range(len(nums)):
  counter[nums[i]].append(i)

total = 0
for _,v in counter.items():
  v = len(v)
  total += (v * (v-1)) // 2

for k in range(len(nums)):
  print(total - (len(counter[nums[k]])-1))

