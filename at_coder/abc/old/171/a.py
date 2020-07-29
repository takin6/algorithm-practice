a = input()
small = list(range(ord("a"), ord("z")+1))
big = list(range(ord("A"), ord("Z")+1))
if ord(a) in small:
  print("a")
else:
  print("A")