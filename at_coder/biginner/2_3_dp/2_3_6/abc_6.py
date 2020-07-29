N = int(input())
import bisect

swapped = 0
LIS = []
for _ in range(N):
  i = int(input())
  if len(LIS) == 0 or i > LIS[-1]:
    LIS.append(i)
  else:
    LIS[bisect.bisect(LIS, i)] = i
    swapped += 1

print(swapped)
