import bisect
N = int(input())
presents = []

for _ in range(N):
  w,h = map(int,input().split())
  presents.append([w,h])

presents.sort(key=lambda x: (x[0],-x[1]))

LIS = [presents[0][1]]
for i in range(1, len(presents)):
  if presents[i][1] > LIS[-1]:
    LIS.append(presents[i][1])
  else:
    LIS[bisect.bisect_left(LIS, presents[i][1])] = presents[i][1] 

print(len(LIS))