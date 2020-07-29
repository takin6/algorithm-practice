def pascal_triangle(i, j):

  if j == 1 or j == i: return 1
  return pascal_triangle(i-1, j-1) + pascal_triangle(i-1, j)

print(pascal_triangle(5, 3))



def pascal_triangle_get_row(n):
    MIN_INF = -500000
    memo = [ [MIN_INF] * 30 for _ in range(30)]
    ans = []
    
    def get_val(r, c):
        if c == 1 or c == r: 
            memo[r][c] = 1
            return memo[r][c]

        if memo[r-1][c-1] != MIN_INF and memo[r-1][c] != MIN_INF:
            memo[r][c] = memo[r-1][c-1] + memo[r-1][c]
            return memo[r][c]
        else:
            return get_val(r-1, c-1) + get_val(r-1, c)

    for c in range(1, n+2):
        ans.append(get_val(n+1, c))

    return ans

print(pascal_triangle_get_row(25))

# recurrence relation
# i = ith row, j = jth column
# f(i, j) = f(i-1, j-1) + f(i-1, j)

# base case
# f(i, j) = 1 if j == 1 or j == i