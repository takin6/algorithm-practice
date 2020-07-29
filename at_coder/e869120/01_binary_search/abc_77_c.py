import bisect
N = int(input())
A = list(map(int,input().split()))
A.sort()
B = list(map(int,input().split()))
C = list(map(int,input().split()))
C.sort()

res = 0
for b in B:
  pairA = bisect.bisect_left(A, b)
  pairC = bisect.bisect_right(C, b)
  res += pairA * (N-pairC)

print(res)
# def binary_search(arr, x):
#   def is_ok(i):
#     if i<0: return True
#     if i>=N: return False
#     return arr[i] <= x

#   ok,ng = -1,len(arr)
#   while abs(ok-ng)>1:
#     mid = (ok+ng)//2
#     if is_ok(mid):
#       ok = mid
#     else:
#       ng = mid
#   return ok,ng

# print(A)
# print(C)
# res = 0
# for i,b in enumerate(B):
#   ok,ng = binary_search(A, b)
#   # print(ok,ng)
#   if ok==-1:
#     pairA = N
#   else:
#     pairA = ok+1

#   ok,ng = binary_search(C, b)
#   if ok==-1:
#     pairC = N
#   else:
#     pairC = N-ng

#   print(b, pairA,pairC)
#   res += pairA*pairC

# print(res)

