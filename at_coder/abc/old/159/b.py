# 1. S is Palindrome
# 2. S[1, (N-1)//2]
# 3. S[(N+3)//2, N]

def is_palindrome(str):
  i, j = 0, len(str)-1
  while i <= j:
    if str[i] != str[j]:
      return False
    i += 1
    j -= 1

  return True

s = input()
n = len(s)
if is_palindrome(s) and is_palindrome(s[0:((n-1)//2)]) and is_palindrome(s[(n+3)//2-1:]):
  print("Yes")
else:
  print("No")
