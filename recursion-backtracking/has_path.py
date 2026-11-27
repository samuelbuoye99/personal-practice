def has_path(grid):
    result = []
    x = len(grid)-1
    y = len(grid[0])-1

    def explore(path, row, col):
        if grid[0][0] == 1:
            return
        
        if (row, col) == (x, y) and grid[row][col] == 0:
            result.append(path[:]+[(row, col)])
            return

        if (row, col) == (0, 0):
            path.append((row, col))
            explore(path, row+1, col)
            explore(path, row, col+1)
            path.pop()

        if row>0 and grid[row][col] == 0 and grid[row-1][col] == 0:
            path.append((row, col))
            if row<x:
                explore(path, row+1, col)
            if col<y:
                explore(path, row, col+1)
            path.pop()

        if col>0 and grid[row][col] == 0 and grid[row][col-1] == 0:
            path.append((row, col))
            if row<x:
                explore(path, row+1, col)
            if col<y:
                explore(path, row, col+1)
            path.pop()

    explore([], 0, 0)
    return result

alll = has_path([[0, 0, 1],
                 [1, 0, 0],
                 [1, 0, 0]])
for path in alll:
    print(path)