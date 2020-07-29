import os

class Solution:
    def reverseString(self, s):
        """
        Do not return anything, modify s in-place instead.
        """
        
        def reverse(i, j):
            if i >= j: return
            else:
                tmp = s[j]
                s[j] = s[i]
                s[i] = tmp
            
            print(i,  j)
            reverse(i+1, j-1)
        
        reverse(0, len(s)-1)
        return s

# print(Solution().reverseString(["h","e","l","l","o"]))

print(Solution().reverseString(["H","a","n","n","a","h"]))