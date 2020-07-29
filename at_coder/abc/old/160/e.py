x,y,a,b,c= list(map(int, input().split()))

A = sorted(list(map(int, input().split())), reverse=True)
A = A[:x]
B = sorted(list(map(int, input().split())), reverse=True)
B = B[:y]

C = sorted(list(map(int, input().split())), reverse=True)

ans = A + B + C
ans = sorted(ans, reverse=True)[:x+y]

print(sum(ans))

