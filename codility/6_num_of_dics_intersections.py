A = [1,5,2,1,4,0]
# openingPoint = []
# closingPoint = []

# for i in range(len(A)):
#   openingPoint.append(i-A[i])
#   closingPoint.append(A[i]+i)

def solution(A):
    circles = []
    for idx, radius in enumerate(A):
        circles.append([idx-radius, 'L'])
        circles.append([idx+radius, 'R'])

    circles.sort(key=lambda x: (x[0], x[1]))
    intersections, actives = 0, 0

    for _, flag in circles:
        if flag == 'L':
            intersections += actives
            actives += 1
        else:
            actives -= 1

        if intersections > 10000000:
            return -1

    return intersections

A = [1,5,2,1,4,0]
print(solution(A))

A = [1,1,1]
print(solution(A))