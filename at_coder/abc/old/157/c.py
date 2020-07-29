# n, m = list(map(int, input().split()))

# num = [None] * n

# for i in range(m):
#   idx, g = list(map(int, input().split()))

#   if num[idx-1] is None:
#     num[idx-1] = g
#   else:
#     num[idx-1] = min(num[idx-1], g)

# ans = ""
# if num[0] == None or (n > 1 and num[0] == 0): 
#   ans = "-1"
#   if n == 0 and num is None: ans = "0"
# else:
#   for i in num:
#     if i == None:
#       ans += "0"
#     else:
#       ans += str(i)

# print(ans)

# for i in range(5):
#   idx, n = list(map(int, input().split()))

#   if num[idx-1] is None:
#     num[idx-1] = n
#   else:
#     num[idx-1] = min(num[idx-1], n)

# print(num)
