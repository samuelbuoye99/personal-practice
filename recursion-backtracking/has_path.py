def has_path(grid):
    result = []

    def explore(path):
        if path and path[0] == (0, 0):
            result.append(path[0])
            return
        if path:
            x, y = path[0]
        if path and result and (result[-1] == (0, 0) or result[-1] == (x-1, y) or result[-1] == (x, y-1)):
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
                [1, 1, 0]]))
print(has_path([[0, 1],
                [1, 0]]))