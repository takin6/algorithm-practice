# 1. swap a and b
# 2. swap a and c
ints = list(map(int, input().split()))
ints[0], ints[1] = ints[1], ints[0]
ints[0], ints[2] = ints[2], ints[0]

print(" ".join([ str(e) for e in ints]))