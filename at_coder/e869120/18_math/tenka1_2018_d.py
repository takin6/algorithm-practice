N = int(input())

# checking to see if N can create S
k = 0 # len of s
for i in range(1,N+1):
  if N==(i*(i+1))//2:
    k = i
    break
if not k:
  print("No")
  exit()

S = [ [0]*k for _ in range(k+1) ]

base,span = 1,k
for i in range(k):
  S[i][i:i+span+1] = list(range(base, base+span))

  for j in range(span):
    S[i+j+1][j] = base+j

  base,span = base+span,span-1

# for s in S:
#   print(s)

print("Yes")
print(k+1)
for s in S:
  print(" ".join([ str(s) for s in [k]+s ]))