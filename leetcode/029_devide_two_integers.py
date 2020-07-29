class Solution:
    def divide(self, dividend: int, divisor: int) -> int:

        # MAX_INT = 2 ** 31 - 1
        # MIN_INT = -2**31

        # if abs(divisor) == 1: 
        #     if divisor < 0: ans = -dividend
        #     ans = dividend
        # else:
        #     ans = 0
        #     count = 1
        #     for i in range(1, dividend+1):
        #         if count == abs(divisor):
        #             ans += 1
        #             count = 1
        #         else:
        #             count += 1

        #     if divisor < 0 and dividend > 0: ans = -ans

        # if ans > MAX_INT: return MAX_INT
        # if ans < MIN_INT: return MIN_INT

        # return ans

        # --- solution ----
        # positive = (dividend < 0) is (divisor < 0)
        # dividend, divisor = abs(dividend), abs(divisor)

        # res = 0
        # while dividend >= divisor:
        #     temp, i = divisor, 1
        #     print("outer", dividend, temp, i)
        #     # import pdb; pdb.set_trace()

        #     while dividend >= temp:
        #         dividend -= temp
        #         res += i
        #         # print("inner")
        #         # import pdb; pdb.set_trace()

        #         i <<= 1
        #         temp <<= 1

        #         print("inner", dividend, temp, i)

        # if not positive: res = -res
        # return min(max(MIN_INT, res),MAX_INT)


        # ------- myans -------------
        positive = (dividend < 0) is (divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)
        # dividend, divisor
        tmpDE = abs(dividend)
        ans = 0

        while tmpDE >= divisor:
            tmpDE -= divisor
            ans += 1

            tmpDS, i = divisor, 1 
            while tmpDE >= tmpDS:
                tmpDE -= tmpDS
                ans += i

                tmpDS <<= 1
                i <<= 1

        if not positive:
            return max(-ans, -2147483648)

        return min(ans, 2147483647)



print(Solution().divide(-2147483648, -1))

# print(Solution().divide(6, 3))

# print(Solution().divide(-1, -1))

# print(Solution().divide(1, 1))

# print(Solution().divide(10, 3))

# print(Solution().divide(7, -3))
