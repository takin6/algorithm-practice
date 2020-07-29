# - city i-1 and i are connected with road
# - len of road btw i-1 and i = pow(a(i-1), a(i))

# city 1->3 : 1->2 + 2->3 = pow(5,3) + pow(3,1)
# city 3->2 : 3->2 = pow(3,1)
# city 2->4 : 2->3 + 3->4 = pow(3,)

# n,p = map(int,input().split())
# A = [0]+list(map(int,input().split()))
# C = list(map(int,input().split()))
# MOD = 10**9+7

# res = 0
# s = 1
# for i in range(p):
#   t = C[i]
#   if s > t:
#     for j in range(s, t, -1):
#       res += (pow(A[j-1], A[j], MOD)) % MOD
#   else:
#     for j in range(s, t):
#       res += (pow(A[j], A[j+1], MOD)) % MOD
#   s = t

# t = 1
# if s > t:
#   for j in range(s, t, -1):
#     res += (pow(A[j-1], A[j], MOD)) % MOD
# else:
#   for j in range(s, t):
#     res += (pow(A[j], A[j+1], MOD)) % MOD

# print(res % MOD)

N,Q = map(int,input().split())
A = list(map(int,input().split()))
C = [1]+list(map(int,input().split()))+[1]
s = [0]*(N+1)
for i in range(N):
  s[i+1] = s[i]+pow(A[i-1],A[i],1000000007)%1000000007
print(s)
ans = 0
for i,c in enumerate(C):
    ans += (s[max(C[i-1],c)]-s[min(C[i-1],c)])%1000000007
print(ans%1000000007)