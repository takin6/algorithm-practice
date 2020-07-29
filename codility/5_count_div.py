def solution(A, B, K):
    # cur = (A-1) // 2
    # divisibles = [cur]
    # for i in range(A, B+1):
    #     if i % K == 0:
    #         cur += 1
    #     divisibles.append(cur)

    # return divisibles[-1] - divisibles[0]
    if A % K == 0:
        return (B-A) // K + 1
    else:
        return (B - (A - A%K)) // K
print(solution(6,11,2))

