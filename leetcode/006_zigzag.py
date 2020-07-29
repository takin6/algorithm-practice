import math


# ------------- 1st attempt -------------
# def zigzag(s, numRows):
#   arr = [ [] ] * N

#   prev = 0
#   loop = math.ceil(len(s) / (len(s) + len(s)-2))

#   cur_idx = 0
#   for i in range(0, loop):
    
#     for j in range(0, N):
#       arr[j].append(s[cur_idx])
#       cur_idx += 1

#     for k in reversed(range(1, N-1)):
#       arr[k].append(s[cur_idx])
#       cur_idx += 1


#     break
#     # for j in range(0, N-2):
#     #   arr[i].append(s[cur_idx])

#   print(arr)

# print(zigzag("PAYPALISHIRING", 3))

# ------------- 2nd attempt -------------


def convert(s: str, numRows: int) -> str:
    arr = [ [] for i in range(numRows)]
    # -1 : going down, 1 going up
    direction = -1
    cur_row = 0

    if numRows == 1: return s

    for char in s:
        arr[cur_row].append(char)

        if cur_row == 0: direction = -1
        if cur_row == numRows-1: direction = 1

        if direction == -1: cur_row += 1
        if direction == 1: cur_row -= 1
    
    ans = ""
    for row in arr:
        for c in row:
            if c != "": ans += c

    return ans


print(convert("ABC", 1))
print(convert("AB", 1))

print(convert("PAYPALISHIRING", 3))


# PAHNAPLSIIGYIR
# PAHNAPLSIIGYIR

# PAIIANPSIYRHLG