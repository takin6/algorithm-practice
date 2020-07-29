from collections import Counter
def solution(A):
    counter = Counter(A)
    
    for key in counter:
        if counter[key] > len(A)//2:
            return A.index(key)
    
    return -1


print(solution([2, 1, 1, 3]))