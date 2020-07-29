# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000

def intToRoman(num):
    # r2i = { 1000: "M", 500: "D", 100: "C", 50: "L", 10: "X", 5: "V", 1: "I"}
    # nums = [1000, 500, 100, 50, 10, 5, 1]
    nums = [ 1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1 ]
    roman = [ "M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I" ]

    ans = ""

    for i in range(len(nums)):
        if num // nums[i] > 0:
            ans += roman[i] * (num // nums[i])
            num = num % nums[i]

    return ans

print(intToRoman(1994))
# Output: "MCMXCIV"
# MDCCCCLXXXXIIII