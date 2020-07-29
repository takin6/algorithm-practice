# 8% => A
# 10% => B

# 税抜き
# 複数存在する場合は最も小さい金額
# => x*0.08=A, x*0.1=B


# x*0.08=2, x*0.1=2
# =>x = 

import math
A, B = list(map(int, input().split()))

# x, y = A / 0.08, B / 0.1

# if math.floor(x) == math.floor(y):
#   print(int(x))
#   exit(0)
# if x > y:
#   tmp = math.floor(x * 0.1)
#   if tmp == B:
#     print(int(x))
#     exit(0)
# else:
#   tmp = math.floor(y * 0.1)
#   if tmp == A:
#     print(int(y))
#     exit(0)

# print(-1)


for x in range(1, 1250):
  if math.floor(x * 0.08) == A and math.floor(x * 0.1) == B:
    print(x)
    exit(0)

print(-1)