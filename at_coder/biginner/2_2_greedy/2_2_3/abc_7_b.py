A = input()
res = ""

for c in A:
  if c == "a":
    res += c
  else:
    res += chr(ord(c)-1)
    break

if res == A and res == "a":
  print(-1)
else:
  print(res[0])