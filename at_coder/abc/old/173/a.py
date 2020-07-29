n = int(input())

i = n%1000
if i != 0:
  print(1000-i)
else:
  print(i)


# while n > 0:
#   n -= 1000

# print(min(-n, 1000+n))


# i = n//1000

# tmp1 = n - (i*1000)
# tmp2 = ((i+1)*1000) - n
# print(min(tmp1, tmp2))

# print(min(n%(1000*i), (1000*(i+1))%n))