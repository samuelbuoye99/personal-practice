def count_routes(rows, cols):
    result = []
    def explore(row, col, path):
        if path and path[-1]==(rows-1, cols-1):
            print(path[:])
            
        for i in range(row, rows):
            for j in range(col, cols):
                if path and (path[-1] != (i-1, j) or path[-1] != (i, j-1)):
                    continue
                if i<rows-1:
                    path.append((i, j))
                    explore(row+1, col, path)
                    path.pop()
                if j<cols-1:
                    path.append((i, j))
                    explore(row, col+1, path)
                    path.pop()

    explore(0, 0, [])
    return result


print(count_routes(3, 3))