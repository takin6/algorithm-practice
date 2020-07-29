
def number_of_islands(grid):

    if not grid or not grid[0]:
        return 0
    MAX_INT = 10 ** 10
    for row in grid:
        row.insert(0, MAX_INT)
        row.append(MAX_INT)
    grid.insert(0, [MAX_INT] * len(grid[0]))
    grid.append([MAX_INT] * len(grid[0]))

    graph = grid
    result = 0
    visited = [ [None] * len(graph[0]) for _ in range(len(graph)) ]

    def dfs(row, col):
        if graph[row][col] == 1:
            visited[row][col] = True
        else:
            return

        directions = [  (row-1, col-1), (row-1,col), (row-1,col+1),
                        (row,col-1), (row,col+1),
                        (row+1,col-1), (row+1,col), (row+1,col+1) ]

        for d in directions:
            r, c = d
            if visited[r][c] is None:
                dfs(r, c)

    for i in range(len(graph)):
        for j in range(len(graph[0])):
            if graph[i][j] == 1 and visited[i][j] is None:
                result += 1
                dfs(i, j)
            else:
                visited[i][j] = True

    return result


# N = 10 ** 10
# graph = [
#   [N, N, N, N, N, N, N],
#   [N, 1, 0, 1, 0, 1, N],
#   [N, 1, 1, 0, 0, 0, N],
#   [N, 1, 1, 0, 1, 0, N],
#   [N, N, N, N, N, N, N],
# ]

# grid = [[1,1,1,1,1,1,1],
#          [1,0,0,0,0,0,1],
#          [1,0,1,1,1,0,1],
#          [1,0,1,0,1,0,1],
#          [1,0,1,1,1,0,1],
#          [1,0,0,0,0,0,1],
#          [1,1,1,1,1,1,1]]
grid = [[1]]

# grid = [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]
print(number_of_islands(grid))
