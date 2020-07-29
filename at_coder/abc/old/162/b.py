
# N = int(input())

# def F(d):
#   n = N // d
#   # import pdb; pdb.set_trace()
#   return 1/2*n*(2*d+(n-1)*d)

# import pdb; pdb.set_trace()
# print( (F(3) + F(5)) - F(15)) 

N = int(input())

res = 0
for i in range(1, N+1):
  if i % 15 == 0 or i % 3 == 0 or i % 5 == 0:
    continue
  res += i

print(res)
