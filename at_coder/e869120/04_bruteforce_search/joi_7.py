# m <= 200
# n <= 1000

# 1000* 200 = 

def LI():
  return list(map(int,input().split()))

def TI():
  return tuple(map(int,input().split()))

m = int(input())
seiza = []
for _ in range(m):
  seiza.append(LI())

n = int(input())
canvas = []
for _ in range(n):
  canvas.append(TI())
scanvas = set(canvas)

pivot_x, pivot_y = seiza[0]
for i in range(n):
  x2,y2 = canvas[i]
  found = True
  for j in range(1, m):
    x,y = seiza[j]
    diff_x,diff_y = x-pivot_x, y-pivot_y
    # print(x,y,diff_x, diff_y)
    if (x2+diff_x,y2+diff_y) in scanvas:
      continue
    else:
      found = False
      break

  if found:
    print(x2-pivot_x,y2-pivot_y)
    exit()
  else:
    continue

