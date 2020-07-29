def solution(K, M, A):
    # write your code in Python 3.6
    l, r = max(A), sum(A)

    while r >= l:
        m = (r + l) // 2

        if ok(m, K, A):
            r = m -1
        else:
            l = m + 1

    return l

def ok(m, K, A):
    block = 1
    cap = 0

    for a in A:
        if cap + a > m:
            block += 1
            cap = a
        else:
            cap += a

    return block <= K

print(solution(3, 6, [5, 2, 3, 4, 6]))
print(solution(1,1,[0]))
print(solution(3,5,[2,1,5,1,2,2,2]))
print(solution(3,1,[1,1,1,1,1,1,1]))
print(solution(2, 10, [4, 4]))