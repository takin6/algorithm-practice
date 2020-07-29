H, N = list(map(int, input().split()))
A = list(map(int, input().split()))

print(sum(A))
if sum(A) >= H:
  print("Yes")
else:
  print("No")