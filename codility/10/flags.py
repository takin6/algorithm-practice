# def solution(A):
#     from math import sqrt
#     N = len(A)
#     peaks, x = find_peaks(A)
#     if len(x) < 2:
#         return len(x)

#     x = int(sqrt(N))
#     for i in range(x+1, 0, -1):
#         if check(i, peaks):
#             return i

#     return 0

# def check(x, peaks):
#     N = len(peaks)
#     flags = x
#     pos = 0

#     while pos < N and flags > 0:
#         if peaks[pos]:
#             flags -= 1
#             pos += x
#         else:
#             pos += 1

#     return flags == 0


# def find_peaks(A):
#     peaks = [False] * len(A)
#     x = []
#     for i in range(1, len(A)-1):
#         if A[i] > A[i-1] and A[i] > A[i+1]:
#             peaks[i] = True
#             x.append(i)

#     return peaks,x


# from math import sqrt
# def solution(A):
#     peaks = []
#     for i in range(1, len(A)-1):
#         if A[i-1] < A[i] > A[i+1]:
#             peaks.append(i)

#     if len(peaks) < 2:
#         return len(peaks)

#     max_flag_count = int(sqrt(len(A)))

#     for flag_num in range(max_flag_count+1, 0, -1):
#         flag_count = 1
#         dist = 0
#         for idx in range(1, len(peaks)):
#             dist += peaks[idx] - peaks[idx-1]
#             if dist >= flag_num:
#                 flag_count += 1
#                 dist = 0
        
#         if flag_count >= flag_num:
#             return flag_num

#     return 0

def solution(A):
    N = len(A)
    if N < 3:
        return 0

    # storing next peaks
    next_peak = [-1]*N

    peak_cnt = 0
    for i in range(N-2, 0, -1):
        if A[i-1] < A[i] and A[i] > A[i+1]:
            next_peak[i] = i
            peak_cnt += 1
        else:
            next_peak[i] = next_peak[i+1]
    next_peak[0] = next_peak[1]

    max_flags = 0
    for i in range(1, peak_cnt+1):
        # the distance between the first flag and the last flag
        # must be smaller than N
        # ex) peaks == [1,4,7] and i == 3 and N = 11
        # 3*(2) + 2 > 11
        if (i-1)*i+2 >= N: break
        pos = 0
        num = 0
        while pos < N and num < i:
            pos = next_peak[pos]
            if pos == -1:
                break
            num += 1
            pos += i

        if num >= i:
            max_flags = num

    return max_flags

# print(solution([1,5,3,4,3,4,1,2,3,4,6,2]))
# print(solution([1,2,3,4,5,6]))
# print(solution([1,3,2]))
print(solution([3,2,1]))