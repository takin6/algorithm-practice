N,K = map(int,input().split())
P = list(map(int,input().split()))
P.sort()

print(sum(P[:K]))

# res = 10**16
# for t in combinations(range(N), K):
#   res = min(res, sum([P[i] for i in t]))
# print(res)




# cumsum = [0]
# for p in P:
#   cumsum.append(cumsum[-1]+p)

# res = 10**15
# for i in range(N-K+1):
#   res = min(res, cumsum[i+K]-cumsum[i])

# print(res)