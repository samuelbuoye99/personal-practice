def has_path(grid: list[list[int]]):
    result = []
    if grid[0][0] == 1:
        return [result]
    
    def explore(path: list, row: int, col: int):
        x = len(grid)
        y = len(grid[0])
        if path:
            result.append(path[:])

        for i in range(row, x):
            for j in range(col, y):
                if grid[i][j]==1:
                    continue
                if path and i>0 and j>0 and (path[-1] != i-1, j or path[-1] != i, j-1):
                    continue
                if path and i>0 and path[-1] != (i-1, j):
                    continue
                if path and j>0 and path[-1] != (i, j-1):
                    continue
                if row<x-1:
                    path.append((i, j))
                    explore(path, row+1, col)
                    path.pop()
                if col<y-1:
                    path.append((i, j))
                    explore(path, row, col+1)
                    path.pop()
    explore([], 0, 0)
    return result


print(has_path([[0, 1, 1],
                [0, 1, 1],
                [0, 0, 0]]))