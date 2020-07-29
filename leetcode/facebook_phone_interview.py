s = "instagram"
# s = "aaaaaaaaa"
# s = "aaaaaa"
# s = "ssssss"
t = "a"

import math
arr = [math.inf] * len(s)

# from left to right
cnt = math.inf
for i in range(len(s)):
  if s[i] == t:
    cnt = 0

  arr[i] = min(arr[i], cnt)
  cnt += 1

# [inf,inf,inf,inf,0,1,2,0,1]

for j in range(len(s)-1, -1, -1):
  if s[j] == t:
    cnt = 0

  arr[j] = min(arr[j], cnt)
  cnt += 1

arr = [ -1 if i == math.inf else i for i in arr ]
print(arr)