# x
# x = abs(x-K)

# start = N
# most monimum value of N

# ex1
# N K
# 7 4
# seen = [7]
# 1. |7-4| = 3
# seen = [7,3]
# 2. |3-4| = 1
# 3. |1-4| = 3 
# 3 is seen
# => 1

# ex2)
# 2 6
# 
# 1. |2-6| = 4
# 2. |4-6| = 2

# ex3)
# 10000000000000


#========================================
# x
# x = abs(x - K)
# if x > K: x-K
# N 

N, K = list(map(int, input().split()))
n = N%K
print(min(n, abs(K-n)))

# if K == 1:
#   print(0)
#   sys.exit()

# seen = [N]
# x = N
# while True:
#   x = abs(x-K)
#   if x == 1:
#     print(1)
#     sys.exit()
#   if x in seen:
#     print(min(seen))
#     sys.exit()
#   else:
#     seen.append(x)

