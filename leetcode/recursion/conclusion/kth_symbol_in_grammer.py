class Solution:
    def kthGrammar(self, N: int, K: int) -> int:
        print(N, K)
        rule = { 0: [0, 1], 1: [1, 0]}
        if N == 1: return 0

        if self.kthGrammar(N-1, K//2+K%2) == 0:
            return rule[0][K%2-1]
        else:
            return rule[1][K%2-1]

print(Solution().kthGrammar(4, 3))