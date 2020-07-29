a,v = map(int,input().split())
b,w = map(int,input().split())
t = int(input())
if v <= w:
  print("NO")
  exit()
d = abs(a-b)
if (v-w)*t >= d:
  print("YES")
else:
  print("NO")

# d = abs(a-b)
# if v <= w:
#   print("NO")
#   exit()

# s = v-w
# if d <= s*t:
#   print("YES")
# else:
#   print("NO")

# if A==B:
#   print("YES")
# else:
#   if V==W:
#     print("NO")
#   else:
#     x = (B-A) / (V-W)
#     if 0 <= x <= T:
#       print("YES")
#     else:
#       print("NO")

# A = A-B
# B = 0

# if A+V*T >= B+W*T:
#   x = (B-A) / (V-W)
#   print(x)
#   if x <= T:
#     print("YES")
#   else:
#     print("NO")
# else:
#   print("NO")


# if A+(V*T) >= W*T:
#   for t in range(1,T+1):
#     if A+(V*t) == W*t:
#       print("YES")
#       exit()
#   print("NO")
# else:
#   print("NO")

# A,V = map(int,input().split())
# B,W = map(int,input().split())
# T = int(input())
# seen = []
# l,r = 0, T
# while r>=l:
#   m = l + (r - l) // 2
#   if m in seen:
#     print("NO")
#     exit()
#   else:
#     seen.append(m)

#   if A+V*m == B+W*m:
#     print("YES")
#     exit()

#   if A+V*m > B+W*m:
#     r = m
#   else:
#     l = m

# print("NO")


# if A==B:
#   print("YES")
#   exit()

# for _ in range(T):
#   A += V
#   B += W
#   if A==B:
#     print("YES")
#     exit()

# print("NO")