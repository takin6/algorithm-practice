def solution(N):
    # write your code in Python 3.6
    i = 1
    result = 0

    while i*i < N:
        if N%i == 0:
            result += 2
        i += 1

    if i*i == N:
        result += 1

    return result

print(solution(24))