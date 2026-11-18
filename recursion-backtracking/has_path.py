def has_path(grid):
    result = []

    def explore(path):
        if path:
            result.append(path[0])

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[0][0]==1:
                    return
                if grid[i][j]==1:
                    continue
                if i>0 and j>0 and grid[i-1][j] != 0 and grid[i][j-1] != 0:
                    continue
                if i<0 and j==0 and grid[i-1][j] != 0:
                    continue
                if j>0 and i==0 and grid[i][j-1] != 0:
                    continue
                if path and (path[-1] != i, j-1 or path[-1] != i-1, j):
                    continue
                path.append((i,j))
                explore(path)
                path.pop()

    explore([])
    return result

print(has_path([[0, 0, 1],
                [1, 0, 0],
                [1, 1, 0]]))
print(has_path([[0, 1],
                [1, 0]]))