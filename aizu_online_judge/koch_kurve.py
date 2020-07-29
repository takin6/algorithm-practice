
# n = 2

# class Edge():
#   def __init__(self, x, y):
#     self.x = x
#     self.y = y


# def koch_kurve(n)
#   edges = []
#   if n == 0:
#     edges.extend([Edge(0, 0), Edge(100, 0)])
#     return
#   else:
#     edges = set()
#     for i in range(len(edges)-1):
#       edges.extend(make_edge_list(edges[i], edges[i+1]))

#   koch_kurve(n-1)

#   result = []
#   for i in range(len(edges)-1):
#     result.extend(make_edge_list(edges[i], edges[i+1]))

#   return result


# def make_edge_list(p1, p2):
#   p1 = edges[0]
#   p2 = edges[1]
#   s = Edge(p2.x * 1/3, p1.y)
#   t = Edge(p2.x * 2/3, p1.y)
#   u = Edge((p1.x+p2.x)/2, t.y-s.y)

#   return [p1, s, u, t, p2]

# koch_kurve(3)

import math

def koch_kurve(n, p1=[0, 0], p2=[100, 0]):
  if n == 0: return

  s, t, u = make_edge_list(p1, p2)

  print("----{0} p1, s------".format(str(n-1)))
  koch_kurve(n-1, p1, s)
  print(" ".join([ str(i) for i in s ]))
  print("----{0} s, u------".format(str(n-1)))
  koch_kurve(n-1, s, u)
  print(" ".join([ str(i) for i in u ]))
  print("----{0} u, t------".format(str(n-1)))
  koch_kurve(n-1, u, t)
  print(" ".join([ str(i) for i in t ]))
  print("----{0} t, p2------".format(str(n-1)))
  koch_kurve(n-1, t, p2)


def make_edge_list(p1, p2):
  sx = 2 / 3 * p1[0] + 1 / 3 * p2[0]
  sy = 2 / 3 * p1[1] + 1 / 3 * p2[1]
  # s = (sx, sy)
  s = [sx, sy]

  tx = 1 / 3 * p1[0] + 2 / 3 * p2[0]
  ty = 1 / 3 * p1[1] + 2 / 3 * p2[1]
  t = [tx, ty]

  theta = math.radians(60)
  ux = math.cos(theta) * (tx - sx) - math.sin(theta) * (ty - sy) + sx
  uy = math.sin(theta) * (tx - sx) + math.cos(theta) * (ty - sy) + sy
  u = [ux, uy]

  return s, t, u

n = int(input())
print("0 0")
koch_kurve(n)
print("100 0")



  # s = [p2[0] * 1/3, p1[1]]
  # t = [p2[0] * 2/3, p1[1]]
  # u = [(p1[0]+p2[0])/2, t[1]-s[1]]
