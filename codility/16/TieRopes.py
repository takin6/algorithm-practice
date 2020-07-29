

def solution(A, K):
    res = 0
    current = 0

    for i in A:
        current += i
        if current >= K:
            current = 0
            res += 1

    return res

print(solution([1,2,3,4,1,1,3], 4))