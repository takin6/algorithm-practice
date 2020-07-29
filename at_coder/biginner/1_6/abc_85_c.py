import sys
N, Y = list(map(int, input().split()))


for i in range(N+1):
  for j in range(N+1):
    z = N - i - j
    if i+j+z > N or z < 0:
      continue

    if 10000*i + 5000*j + 1000*z == Y:
      print("{0} {1} {2}".format(i,j,z))
      sys.exit()

print("-1 -1 -1")