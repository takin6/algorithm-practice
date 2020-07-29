'''
nucleotide
A,C,G,T
1,2,3,4

What is the minimum impact factor of nucleotides 
contained in a particular part of th given sequence?

N characters
M queiries (p, Q)

Kth query requires yout to find the minimal impact factor of nucleotides
contained in the seq betwen P[K] / Q[J]

'''

S = "CAGCCTA"
P = [2,5,0]
Q = [4,5,6]

M=3

def solution(S,P,Q):
    # M = len(P)
    # res = []
    # for i in range(M):
    #     seq = set(S[P[i]:Q[i]])
    #     if "A" in seq:
    #         res.append(1)
    #     elif "C" in seq:
    #         res.append(2)
    #     elif "G" in seq:
    #         res.append(3)
    #     else:
    #         res.append(4)

    # return res

    # 1. create cumultaive sum
    #   how many types are occuring at ith indexes
    
    cost = {"A": 1, "C": 2, "G": 3, "T": 4}

    count = [0,0,0,0]
    counts = [count[:]]
    for s in S:
        count[cost[s]-1] += 1
        counts.append(count[:])

    res = []
    for i in range(len(P)):
        count_p, count_q = counts[P[i]], counts[Q[i]+1]
        if P[i] == Q[i]:
            res.append(cost[S[P[i]]])
        elif count_q[0] > count_p[0]:
            res.append(1)
        elif count_q[1] > count_p[1]:
            res.append(2)
        elif count_q[2] > count_p[2]:
            res.append(3)
        else:
            res.append(4)

    return res

print(solution('AC', [0, 0, 1], [0, 1, 1]))
print(solution("A", [0], [0]))
print(solution("CAGCCTA", [2,5,0], [4,5,6]))
