
N = int(input())
res = float('inf')
for i in range(1,int(N**0.5)+1):
  if N%i==0:
    x,y = i-1,N//i-1
    res = min(res, x+y)

print(res)

# factors = []
# i = 2
# num = N
# while i*i <= num:
#   if num%i==0:
#     while num%i==0:
#       factors.append(i)
#       num //= i
#   i += 1
# if num != 1:
#   factors.append(num)

# if len(factors) == 1:
#   print(N-1)
#   exit()

# x,y = 1,1
# l,r = 0, len(factors)-1
# while l < r:
#   x *= factors[l]
#   y *= factors[r]
#   l += 1
#   r -= 1
# if len(factors)%2==1:
#   x *= factors[l]

# print(factors)
# print(x-1+y-1)