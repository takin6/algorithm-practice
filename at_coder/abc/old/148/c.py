x,y = [ int(i) for i in input().split(" ") ]

start = 2

a, b = x, y
while a != b:
  temp = abs(a - b)
  a = min(a, b)
  b = temp


ans = x * y / a

print(int(ans))