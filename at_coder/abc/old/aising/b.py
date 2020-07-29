N = int(input())
A = list(map(int,input().split()))

res = 0
for i,a in enumerate(A):
  idx = i+1
  if idx%2==1 and a%2==1:
    res += 1

print(res)