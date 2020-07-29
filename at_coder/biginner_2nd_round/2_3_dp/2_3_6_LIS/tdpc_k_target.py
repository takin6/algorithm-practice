import bisect
N = int(input())
circles = []

for _ in range(N):
  center,radius = map(int,input().split())
  circles.append([center-radius, center+radius])
circles.sort(key=lambda x: (-x[0],-x[1]))

LIS = [circles[0][1]]
for i in range(len(circles)):
  c = circles[i][1]
  if c > LIS[-1]:
    LIS.append(c)
  else:
    LIS[bisect.bisect_left(LIS, c)] = c

print(len(LIS) if len(LIS)>0 else 0)