N = int(input())
x,l = [],[]
for _ in range(N):
  t1,t2 = list(map(int, input().split()))
  x.append(t1)
  l.append(t2)

width = []
for i in range(N):
  width.append([x[i]-l[i],x[i]+l[i]])

width = sorted(width, key=lambda x: x[1])
res = N
for i in range(1, N):
  if width[i-1][1] > width[i][0]:
    width[i][1] = width[i-1][1]
    res -= 1

print(res)
