
# def solution(A, B):
#     lad_seq = []
#     for i in range(0, max(A)+1):
#         if i in (0,1):
#             lad_seq.append(1)
#         else:
#             lad_seq.append(lad_seq[-1] + lad_seq[-2])

    
#     res = []
#     for i in range(len(A)):
#         res.append(lad_seq[A[i]] % 2**B[i])

#     return res

def solution(A, B):
    # https://stackoverflow.com/questions/6670715/mod-of-power-2-on-bitwise-operators/6670766#6670766
    lad_seq = [1,2]
    for i in range(2, max(A)+1):
        lad_seq.append(lad_seq[-1] + lad_seq[-2])

    
    res = []
    for i in range(len(A)):
        res.append(lad_seq[A[i]-1] & pow(2, B[i])-1 )
    
    return res
    
print(solution([4,4,5,5,1], [3,2,4,3,1]))