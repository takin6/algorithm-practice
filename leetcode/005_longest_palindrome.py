
# print(Solution().longestPalindrome("abcda"))

# print(Solution().longestPalindrome("babad"))

# ------------------- brute force approach -----------------------------
# def longestPalindrome(s):
#     ans = ""

#     for i in range(1, len(s)+1):
#         if i == 1:
#             ans = s[0]
#             continue
#         else:
#             for j in range(0, len(s)-i+1):
#                 if isPalindrome(s[j:i+j]):
#                     ans = s[j:i+j]
#                     break

#     return ans

# def isPalindrome(s):
#     # "ana" == palidrome
#     result = True
#     ridx = [i for i in reversed(range(len(s)))]
#     for i in range(len(s)):
#         # if s == "ana": import pdb; pdb.set_trace()
#         if s[i] != s[ridx[i]]:
#             result = False
#             break

#     return result

# print(longestPalindrome("ibvjkmpyzsifuxcabqqpahjdeuzaybqsrsmbfplxycsafogotliyvhxjtkrbzqxlyfwujzhkdafhebvsdhkkdbhlhmaoxmbkqiwiusngkbdhlvxdyvnjrzvxmukvdfobzlmvnbnilnsyrgoygfdzjlymhprcpxsnxpcafctikxxybcusgjwmfklkffehbvlhvxfiddznwumxosomfbgxoruoqrhezgsgidgcfzbtdftjxeahriirqgxbhicoxavquhbkaomrroghdnfkknyigsluqebaqrtcwgmlnvmxoagisdmsokeznjsnwpxygjjptvyjjkbmkxvlivinmpnpxgmmorkasebngirckqcawgevljplkkgextudqaodwqmfljljhrujoerycoojwwgtklypicgkyaboqjfivbeqdlonxeidgxsyzugkntoevwfuxovazcyayvwbcqswzhytlmtmrtwpikgacnpkbwgfmpavzyjoxughwhvlsxsgttbcyrlkaarngeoaldsdtjncivhcfsaohmdhgbwkuemcembmlwbwquxfaiukoqvzmgoeppieztdacvwngbkcxknbytvztodbfnjhbtwpjlzuajnlzfmmujhcggpdcwdquutdiubgcvnxvgspmfumeqrofewynizvynavjzkbpkuxxvkjujectdyfwygnfsukvzflcuxxzvxzravzznpxttduajhbsyiywpqunnarabcroljwcbdydagachbobkcvudkoddldaucwruobfylfhyvjuynjrosxczgjwudpxaqwnboxgxybnngxxhibesiaxkicinikzzmonftqkcudlzfzutplbycejmkpxcygsafzkgudy"))

def longestPalindrome(s):
    dp = [[False]*len(s) for i in range(len(s))]
    beginIdx = None
    max_len = None

    for i in range(0, len(s)): 
        dp[i][i] = True
        beginIdx = i
        max_len = 1

    for i in range(0, len(s)-1):
        if s[i] == s[i+1]:
            dp[i][i+1] = True
            beginIdx = i
            max_len = 2

    for cur_len in range(3, len(s)+1):
        # current index of str
        for i in range(len(s)-cur_len+1):
            print(cur_len, i)
            j = i+cur_len-1
            if cur_len == 4 and i == 3: import pdb; pdb.set_trace()
            if s[i] == s[j] and dp[i+1][j-1]:
                dp[i][j] = True
                beginIdx = i
                max_len = cur_len

    if beginIdx == None and max_len == None:
        return ""
    else:
        return s[beginIdx:beginIdx+max_len]

print(longestPalindrome("bb"))

# print(longestPalindrome("babad"))
# print(longestPalindrome("banana"))

