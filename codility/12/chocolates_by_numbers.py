def solution(N, M):
    res = 1
    X = 0
    while (X+M)%N != 0:
        X = (X+M)%N
        res += 1
    return res

# print(solution(10,4))
print(solution(4,4))