from collections import Counter
def solution(N):
    binary = bin(N)[2:]
    c = Counter(binary)
    if c["1"] == len(binary) or c["1"] < 1:
        return 0

    res = 0
    for _ in range(c["1"]):
        f = binary.find("1")

        if binary[f+1:].find("1") == -1:
            return res
        
        l = binary[f+1:].find("1")-f+1
        res = max(res, l-f-1)
        
        binary = binary[l:]
    
    return res

print(solution(529))
print(solution(1041))