class Solution:
    def myPow(self, x: float, n: int) -> float:
        # ans = 1
        # for i in range(1, n+1):
        #     return ans ** x

        # recurrence relation
        # f(x, n) = f(x, n-1) * f(x, n-2) .... f(x, 1)

        # --- recursive solution: maximum recursion depth -----
        # def helper(num):
        #     if num == 0: return 1
        #     if num == 1: return x
        #     return x * helper(num-1)

        # if n < 0: x = x ** -1
        # return helper(abs(n))


        # --- recusive solution -------
        # 
        def helper(a, b, memo):
            print()
            if b == 0: return 1           
            half = helper(a, b//2)
            if b % 2 == 0:
                memo[b] = half * half
                return memo[b]
            else:
                memo[b] = half * half * a
                return memo[b]

        if n < 0: x = 1 / x
        return helper(x, abs(n), memo)


print(Solution().myPow(2.0000, 10))
# print(Solution().myPow(2.1000, 3))
# print(Solution().myPow(2.0000, -2))
# print(Solution().myPow(1.00001, 123456))
# print(Solution().myPow(0.00001, 2147483647))
