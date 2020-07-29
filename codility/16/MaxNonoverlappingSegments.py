

def solution(A, B):
    if len(A) == 0: return 0
    spans = sorted(zip(A,B), key=lambda x: x[1])
    cnt = 1

    for i in range(1, len(spans)):
        if spans[i-1][1] >= spans[i][0]:
            spans[i] = (spans[i][0], spans[i-1][1])
        else:
            cnt += 1

    return cnt

print(solution([1,3,7,9,9], [5,6,8,9,10]))
