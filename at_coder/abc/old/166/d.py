X = int(input())

MAX_INT = 201

res = 0

for i in range(MAX_INT):
  for j in range(MAX_INT):
    if i**5 - j**5 == X:
      print(i,j)
      exit()

    if i**5 + j**5 == X:
      print(i,-j)
      exit()

# for i in range(1, MAX_INT):
#   for j in range(1, i):
#     if 