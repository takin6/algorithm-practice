import math
N = int(input())
D = list(map(int,input().split()))
D.sort()

l,r = D[N//2-1],D[N//2]
if l==r:
  print(0)
  exit()

print(r-l)

# median = math.ceil((D[N//2]+D[N//2-1]) / 2)
# import pdb; pdb.set_trace()
# print((D[N//2] - median) + 1)