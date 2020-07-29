import bisect
N = int(input())
C = []
for i in range(N):
  C.append(int(input()))

swapped = 0
LIS = [C[0]]
for i in range(1,N):
  if C[i] >= LIS[-1]:
    LIS.append(C[i])
  else:
    LIS[bisect.bisect_left(LIS, C[i])] = C[i]
    swapped += 1

print(swapped)