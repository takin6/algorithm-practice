s=input().split()
n,m,q=int(s[0]),int(s[1]),int(s[2])
cs = [[0]*(n+1) for _ in range(n+1)]

for _ in range(m):
  l,r = map(int,input().split())
  cs[l][r] += 1

for i in range(1,n+1):
  for j in range(1,n+1):
    cs[i][j] += cs[i][j-1]

print(B)
for _ in range(q):
  p,q = map(int,input().split())
  import pdb; pdb.set_trace()
  t = 0
  for i in range(p, q+1):
    t += cs[i][q] - cs[i][i-1]
  print(B[p][q] - B[p-1][q] - B[p][q-1] + B[p-1][q-1])


# arr=[[0 for i in range(n+3)] for j in range(n+3)]
# for i in range(m):
#   s=input().split()
#   l,r=int(s[0]),int(s[1])
#   for j in range(l+1):
#     arr[j][r]+=1

# print(arr)
# for i in range(q):
#   s=input().split()
#   p,q=int(s[0]),int(s[1])
#   print(sum(arr[p][1:q+1]))

[[0, 0, 0, 0, 0, 1, 2, 3, 1, 2, 1, 0, 0],
 [0, 0, 0, 0, 0, 1, 2, 3, 1, 2, 1, 0, 0],
 [0, 0, 0, 0, 0, 1, 1, 3, 1, 2, 1, 0, 0],
 [0, 0, 0, 0, 0, 1, 1, 3, 1, 1, 1, 0, 0],
 [0, 0, 0, 0, 0, 1, 1, 3, 1, 1, 1, 0, 0], 
 [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0], 
 [0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0], 
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0], 
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0], 
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0], 
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0]]