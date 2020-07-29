
# ----- 1st attempt --------------------
# def maxArea(height):
#     ans = 0

#     for i in range(len(height)-1):
#         dis2edge = min(height[i], height[-1]) * (len(height)-1-i)

#         maxHeight = max(height[i+1:])
#         idx = None
#         for k in reversed(range(i+1, len(height))):
#             if height[k] == maxHeight:
#                 idx = k
#                 break

#         dis2max = min(height[i], height[idx]) * (idx-i)

#         ans = max(ans, max(dis2edge, dis2max))
#         print(ans)

#     return ans


# ------ 2nd attempt ---------------
def maxArea(height):
    i = 0
    p = len(height)-1
    ans = 0

    # print("i", "p", "ans")
    while True:
        # print(i, p, ans)
        ans = max(ans, (p-i)*min(height[i], height[p]))

        if height[i] > height[p]:
            p = p -1 
        else:
            i = i + 1

        if p == i: break

    return ans

print(maxArea([1,8,6,2,5,4,8,3,7]))
print(maxArea([10,9,8,7,6,5,4,3,2,1]))