# N = int(input())
# ints = list(map(int, input().split()))

# def T(large, small):
#   if len(large) == 0 or len(small) == 0: return 0
#   if len(large) == 1 and len(small) == 1: return sum(large)+sum(small)

#   s = min(large)
#   next_large = large[:]
#   next_large.pop(next_large.index(s))
#   return sum(large) + sum(small) + T(next_large, [s])

# small = min(ints)
# large = ints[:]
# large.pop(large.index(small))
# print(sum(ints) + T(large, [small]))

N = int(input())
ints = list(map(int, input().split()))
ints = sorted(ints)

cum_sum = [0] * (N+1)
for i in range(N):
  cum_sum[i+1] = cum_sum[i] + ints[i]

res = sum(ints)
for i in range(1,N):
  res += ints[i-1] + (cum_sum[-1]-cum_sum[i])

print(res)

# res = sum(ints)
# for i in range(N-1):
#   if i + 1 < N:
#     res += sum(ints[i+1:])
#   res += ints[i]

# print(res)


# >>> sum([8,10,2,5,6,2,4,7,2,1])
# 47
# >>> sum([1]) + sum([8,10,2,5,6,2,4,7,2])
# 47
# >>> sum([2]) + sum([8,10,2,5,6,2,4,7])
# 46
# >>> sum([2]) + sum([8,10,2,5,6,4,7])
# 44
# >>> sum([2]) + sum([8,10,5,6,4,7])
# 42
# >>> sum([4]) + sum([8,10,5,6,7])
# 40
# >>> sum([5]) + sum([8,10,6,7])
# 36
# >>> sum([6]) + sum([8,10,7])
# 31
# >>> sum([7]) + sum([8,10])
# 25
# >>> sum([8]) + sum([10])
# 18
# >>> 47*2+46+44+42+40+36+31+25+18
# 286+47 = 334