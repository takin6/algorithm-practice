class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        from itertools import zip_longest
        
        def last_valid_char(s):
            skip = 0
            for c in s:
                if c != "#":
                    if skip == 0:
                        yield c
                    else:
                        skip -= 1
                else:
                    skip += 1
        
        print([ (x, y) for x, y in zip_longest(last_valid_char(S[::-1]), last_valid_char(T[::-1]))])
        return all([ x == y for x, y in zip_longest(last_valid_char(S[::-1]), last_valid_char(T[::-1]))])

print(Solution().backspaceCompare("ab#c", "ad#c")) 
print(Solution().backspaceCompare("ab##", "c#d#")) 