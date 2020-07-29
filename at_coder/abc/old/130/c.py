W,H,x,y = map(int,input().split())

n = (W*H)/2
if W == x*2 and H == y*2:
  print(n, 1)
else:
  print(n, 0)

# print(x*2)
# horizontal = [W*(H-y),W*y]
# vertical = [(W-x)*H, x*H]
# import pdb; pdb.set_trace()
# if max(horizontal) > max(vertical):
#   print(min(vertical), 0)
# elif max(horizontal) < max(vertical):
#   print(min(horizontal), 0)
# else:
#   print(min(min(horizontal),min(vertical)), 1)

# if W*(H-y) > (W-x)*H:
#   print((W-x)*H, 0)
# elif W*(H-y) < (W-x)*H:
#   print(W*(H-y), 0)
# else:
#   print(W*(H-y), 1)


# 117928222000000000
# 500000000000000000