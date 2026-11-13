def has_path(grid):
    result = []

    def explore(path):
        if path:
            result.append(path[0])
            return

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[0][0]==1:
                    return
                if grid[i][j]==1:
                    continue
                if i<len(grid)-1 and j<len(grid[i])-1 and grid[i+1][j]==1 and grid[i][j+1]==1:
                    continue
                if i<len(grid)-1 and j==len(grid[i])-1 and grid[i+1][j]==1:
                    continue
                if j<len(grid[i])-1 and i==len(grid)-1 and grid[i][j+1]==1:
                    continue
                path.append((i,j))
                explore(path)
                path.pop()

    explore([])
    return result

print(has_path([[0, 0, 1],
                [1, 0, 0],
                [1, 0, 0]]))
print(has_path([[0, 1],
                [1, 0]]))