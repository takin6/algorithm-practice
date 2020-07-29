n = int(input())
arr = [ int(i) for i in input().split(" ") ]

tmp = 2**30

ans = 0
for ele in arr:
  if tmp > ele:
    ans += 1
    tmp = ele

print(ans)


# for i in range(1, len(arr)):

#   # for j in arr[:i+1]:
#   #   if arr[i] >= j:
#   #     print(arr[i], j)
#   #     ans += 1
#   #     break

#   for j in range(1, i+1):
#     if arr[i-1] > arr[j-1]:
#       print(arr[i-1], arr[j-1])
#       ans += 1
#       break

# print(ans)


# 1...,N P1....Pn
# j (1 <= j <= i), Pi <= Pj