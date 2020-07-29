# import math
# a,b = map(float,input().split())
# import pdb; pdb.set_trace()
# print(int(math.floor(a*b)))

# # 1.1 9.99

# a,b = map(float,input().split())
# a = int(a)
# d = b - int(b)

# res = 0
# for i in range(int(b)):
#   res += a

# res += a*d

# print(int(res))

import decimal

a,b = map(str, input().split())
split_b = b.split(".")
a = int(a)

res = a*int(split_b[0])
f = decimal.Decimal(a) * (decimal.Decimal(split_b[1]) * decimal.Decimal('.01'))

print(res + int(f))