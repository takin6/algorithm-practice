class Solution:
    def __init__(self):
        self.memo = [None] * 100
        self.memo[0] = 0
        self.memo[1] = 1

    # def fib(self, N: int) -> int:
    #     if self.memo[N] is not None: return self.memo[N]

    #     if N < 2:
    #         result = N
    #     else:
    #         result = self.fib(N-1) + self.fib(N-2)

    #     self.memo[N] = result

    #     return result

    def fib(self, N: int) -> int:
        if self.memo[N] is not None:
            return self.memo[N]

        self.memo[N] = self.fib(N-1) + self.fib(N-2)
        return self.memo[N]

# print(Solution().fib(3))
print(Solution().fib(30))