# working day: K / N
# C S
# - # days btn work and work is C
# - if S[i] == 'x', next_work = days[i] + i
# 必ず働く日

# N K C
# 11 3 2
# ooxxxoxxoo
# [1,6,10], [1,6,11], [2,6,10], [2,6,11]

# 5 2 3
# ooxoo
# [1,4]



n, k, c = map(int, input().split())
s = input()
 
foreward = [0] * (k + 1)
backward = [0] * (k + 1)
 
# foreward check
day = 1
i = 0
while i < n and 0 < day <= k:
    if s[i] == "o":
        foreward[day] = i
        i += c
        day += 1
    i += 1
 
# backward check
day = k
i = n - 1
while 0 <= i and 0 < day <= k:
    if s[i] == "o":
        backward[day] = i
        i -= c
        day -= 1
    i -= 1

print(foreward)
print(backward)
for day in range(1, k + 1):
    if foreward[day] == backward[day]:
        print(foreward[day] + 1)