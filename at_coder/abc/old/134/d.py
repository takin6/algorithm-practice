# N = int(input())
# A = list(map(int,input().split()))

# boxes = [ [] for _ in range(N+1) ]
# # import pdb; pdb.set_trace()
# # for i,a in enumerate(A)[::-1]:
# for i in range(N-1,-1,-1):
#   a = A[i]
#   idx = i+1
#   if a == 1:
#     boxes[idx].append(idx)
#     d = 2
#     while idx//d > 0:
#       if idx%d == 0:
#         boxes[idx//d].append(idx)
#       d += 1

# for i in range(1,N+1):
#   idx = i
#   if len(boxes[i]) % idx == A[i-1]:
#     print(idx)
#     print(" ".join(map(str, boxes[i])))
#     exit()
# else:
#   print(-1)

N = int(input())
# A = list(map(int,input().split()))
A = [-1] + list(map(int,input().split()))
B = [0] * (N+1)
for i in range(N, 0, -1):
  tmp = 0
  for j in range(2*i, N+1, i):
    tmp += B[j]
  if tmp%2 != A[i]:
    B[i] = 1

print(B.count(1))
if B.count(1) > 0:
  print(" ".join(map(str, [ i for i,b in enumerate(B) if b==1 ])))
# print(B)

  # a = A[i-1]
  # j = 2
  # prev = 0
  # while i*j < (N+1):
  #   prev ^= A[i*j-1]
  #   j += 1
  # B[i] = a ^ prev
