from fractions import gcd
N = int(input())
A = list(map(int,input().split()))
MOD = 10**9+7
 
def lcm(a,b):
  g = gcd(a, b)
  return a*b // g
 
l = 1
for a in A:
  l = lcm(l, a)
 
# print(l)
 
ans = 0
for a in A:
  ans += l//a
  # ans %= MOD
 
print(ans%MOD)