class Solution:
    def findSubstringInWraproundString(self, p: str) -> int:
        # if len(p) < 2:
        #     return len(p)

        # # seen = set()
        # seen = dict()
        # dp = [ [False] * len(p) for _ in range(len(p)) ]
        # count = 0

        # for i in range(len(p)):
        #     if p[i] not in seen:
        #         count += 1
        #         # seen.add(p[i])
        #         seen[p[i]] = True
        #     dp[i][i] = True
        
        # for span in range(1, len(p)):
        #     for i in range(len(p)):
        #         j = (span + i)
        #         if j >= len(p): continue
        #         if p[i:j+1] in seen:
        #             dp[i][j] = seen[p[i:j+1]]
        #             continue
                
        #         if p[j-1] != "z":
        #             if ord(p[j-1])+1 == ord(p[j]):
        #                 if dp[i+1][j] and dp[i][j-1]:
        #                     dp[i][j] = True
        #                     if p[i:j+1] not in seen:
        #                         count += 1
        #                         seen[p[i:j+1]] = True
        #                         # seen.add(p[i:j+1])
        #         else:
        #             if p[j] == "a":
        #                 if dp[i+1][j] and dp[i][j-1]:
        #                     dp[i][j] = True
        #                     if p[i:j+1] not in seen:
        #                         count += 1
        #                         seen[p[i:j+1]] = True
        #                         # seen.add(p[i:j+1])

        # return count
        from collections import defaultdict
        L = len(p)
        if L == 0: return 0
        dp = [1] * L
        dic = defaultdict(int)
        dic[p[0]] = 1
        for i in range(1, L):
            if ord(p[i]) - ord(p[i-1]) == 1 or p[i] == "a" and p[i-1] == "z":
                dp[i] = dp[i-1]+1
            else:
                dp[i] = 1
            dic[p[i]] = max(dic[p[i]], dp[i])
        return sum(dic.values())

print(Solution().findSubstringInWraproundString("abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"))
print(Solution().findSubstringInWraproundString("tuvwxbcdqrabfghijklmnopqrstuvwxyjklmnohijklmnopqnopqrstudefghijkjklmnopqnopqrstuklmabcdefghefghijdefghijklmnopqropqrstuvwxyzhijklmnopqrsthijklmnopqrsabcdefghijklmnopqrstqrstuvwefghighijklmnopqrstughijklmnopqqrstuvwxyzbcdabcdefghijklmnopqqrstuvwxyefghijklmnopqrstuvcdefefmnopqlmnopqrfghijklmnopqrstuvwxvwdeffghijklmnopqrstuvwxyrstuvwxyzhijklmnopqrsstuklmnopqrstuhijklmcdefghijklmnoplmnopqijklmnopqrsijklmnopqrstucdefghijklijklmhijklmnopqrstuvwmnopqrklmnoiijklmnobcdefghijklmqrstuvwxyfghijklrstuvwxyefghijklmnopqrsghijklmnopqrstuvopqabcdefklmnmnoprstfghijklmnopqrshijklmnopqrstbcdefghijklmnopqrstuvmnopqrstuvwxyzmnopqrstuvcdefghijjklmnopqrstuvwxymnopqrstuvwxmnopqropqrstuvwxcdefgcdefghijklmnopqrstuvwxybcdefghijkdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwfghijklmnopqrstjkijklmbcdefghijklmnopqcdefghijklmnomnopqrstefghijklmnopqrstlmnopqrstuvwxycdefghijklcdefghijklmnopqrstuvwxycdefghijklmnopqrstuvwxdefghighijklrstuvcdefghijklmnopqbcdefgh"))