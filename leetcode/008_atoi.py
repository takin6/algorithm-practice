def myAtoi(s: str) -> int:
    # arr = [ char for char in s if char != " "]
    arr = list(s.strip())

    numeric = [ str(i) for i in range(10) ]
    exp = ["-", "+"]
    # returning 0
    # case1: +- or -+
    # case2: - or +
    # caes3: +x123 or -y123
    if len(arr) == 0 : return 0
    if arr[0] not in numeric and arr[0] not in exp: return 0
    if arr[0] in exp:
        if len(arr) == 1 or arr[1] not in numeric: return 0

    # -111111111111x
    num = ""
    num += arr[0]
    for s in arr[1:]:
        if s not in numeric: break
        num += s

    # The largest value it can represent is (2^31) - 1.
    # The smallest value it can represent is -(2^31).
    INT_MAX = (2**31)-1
    INT_MIN = -(2**31)

    ans = int(num)
    if ans > INT_MAX: return INT_MAX
    if ans < INT_MIN: return INT_MIN

    return ans

print(myAtoi("    -42"))
print(myAtoi("4193 with words"))
print(myAtoi("words and 987"))
print(myAtoi("-91283472332"))
print(myAtoi(""))
print(myAtoi("-"))
print(myAtoi("+1"))
print(myAtoi("-000000000000001")) # => -1
print(myAtoi("+-2"))
print(myAtoi("   +0 123"))