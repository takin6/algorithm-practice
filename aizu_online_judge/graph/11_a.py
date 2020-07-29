n = int(input())
adj_list = [ [0]*n for _ in range(n) ]

for _ in range(n):
    lst = list(map(int, input().split()))
    
    x = lst[0] - 1
    
    if lst[1] == 0:
        continue
    
    for y in lst[2:]:
        adj_list[x][y-1] = 1
    
for r in adj_list:
    print(" ".join([ str(v) for v in r]))