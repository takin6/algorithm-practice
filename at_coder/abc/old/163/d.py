N, K = map(int, input().split())
MAX = 10 ** 9 + 7

res = 0

def calc_sum(l, r):
  return ((l+r) * (r-l+1)) // 2

for i in range(K, N+2):
  low = calc_sum(0,i-1)
  high = calc_sum(N-i+1,N)
  res = (res + (high-low+1)) % MAX

print(res)


# x = K, K+1, K+2, N+1個選んだ時にありうる和を求める

# N=3, 
# K=2,3,4

# low,high = 0,0

# x=1
# 0,1,2,3
# low += x-1 = 0
# high+= N-1+1 = 3
# (high-low)+1 = 4
# 
# x=2
# 1,2,3,4,5
# low += x-1 = 0+1
# high+= 3-2+1= 3+2=5
# (high-low)+1 = 5

# N=3, K=2
# 