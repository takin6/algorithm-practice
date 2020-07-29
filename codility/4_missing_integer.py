from collections import Counter
def solution(A):
    c = Counter(A)
    i = 1
    while True:
        if c[i] == 0:
            return i
        i += 1

# print(solution([1,3,6,4,1,2]))
# print(solution([-1,-3]))

def solution(A):
    N = len(A)
    S = (N*(N+1)) // 2
    s = set()
    for i in A:
        S -= i
        s.add(i)

    if S == 0 and len(s) == len(A):
        return 1
    else:
        return 0

print(solution([4,1,3]))

print(solution([2,2,1,3,2]))
