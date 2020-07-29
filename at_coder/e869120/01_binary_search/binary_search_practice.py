# ok,ng = 10,-1 # さっきと逆なので注意
# while ok-ng > 1: # さっきと逆なので注意。abs(ok-ng)のように汎用的に書く流派もある
#     mid = (ok+ng) // 2 # 平均(小数切り捨て)
#     if is_ok(mid):
#         ok = mid
#     else:
#       ng = mid

# print(ok,ng)

def is_ok(i):
  return i > 5 #大きい側がTrue

ok = -1
ng = 10
while ng-ok > 1:
    mid = (ok+ng) // 2 # 平均(小数切り捨て)
    print(mid)
    # import pdb; pdb.set_trace()
    if is_ok(mid):
      ok = mid
    else:
      ng = mid
print(ok,ng)