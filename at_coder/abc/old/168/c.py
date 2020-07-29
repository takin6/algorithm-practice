import math
A,B,H,M = map(int,input().split())

h_deg = H*30 + M*0.5
m_deg = M*6
rad = math.radians(abs(h_deg - m_deg))

# 余弦定理
print(math.sqrt(A**2 + B**2 - 2*A*B*math.cos(rad)))

# https://note.com/nanigashi/n/n09e6cc649a02
# 角度を求める

# radian：円弧の長さから角度を求める方法
# https://kenyu-life.com/2019/01/09/rad/

# minute,hour = 6,30
# if H==0:
#   if minute*M > 180:
#     hour_angle = 0
#   else:
#     hour_angle = 360
# else:
#   hour_angle = H*hour

# angle = abs(minute*M - hour_angle)
# print(angle)

# print(math.sqrt(A**2 + B**2 - 2*A*B*math.cos(angle)))