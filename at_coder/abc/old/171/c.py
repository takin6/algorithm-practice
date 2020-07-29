# 26
# 26**2
# 26**3

# 1000000000000001
# 3670344486987776

# abcdefghij

N = int(input())
alphas = [ chr(i) for i in range(ord("a"), ord("z")+1)]

res = ""
while N != 0:
  ch = N % 26
  if ch==0:
    res += alphas[-1]
    N = N//26
    N -= 1
  else:
    res += alphas[ch-1]
    N = N//26

print(res[::-1])