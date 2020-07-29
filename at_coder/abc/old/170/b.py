# tsuru: 2
# kame: 4

# total: X, foot: Y
# is it possible??

X,Y = map(int,input().split())

for i in range(101):
  for j in range(101):
    if i*4+j*2 == Y and i+j==X:
      print("Yes")
      exit()

print("No")