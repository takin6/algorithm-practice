N = int(input())

A,B = [],[]
for _ in range(N):
  a,b = map(int,input().split())
  A.append(a)
  B.append(b)

A.sort()
B.sort()

if N%2==0:
  # import pdb; pdb.set_trace()
  medianA = (A[N//2] + A[N//2-1])
  medianB = (B[N//2] + B[N//2-1])
else:
  medianA = A[N//2] 
  medianB = B[N//2]

print(int(medianB-medianA+1))
# print(medianA, medianB)