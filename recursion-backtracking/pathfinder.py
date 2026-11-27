def all_paths(grid: list[list]):
    result = []
    x = len(grid)-1
    y = len(grid[0])-1

    def explore(path: list[tuple], row: int, col: int):
        if (row, col) == (x, y):
            result.append(path[:])
            return

        path.append((row, col))
        if row<x:
            explore(path, row+1, col)

        if col<y:
            explore(path, row, col+1)
        path.pop()

    explore([], 0, 0)
    return result

all = all_paths([[0, 0, 1],
           [1, 0, 0],
           [1, 1, 0]])
print(len(all))
for path in all:
    print(path)


# def all_paths(grid: list):
#     result = []
#     x = len(grid)-1
#     y = len(grid[0])-1

#     def explore(path: list, row: int, col: int):
#         if (row, col) == (x, y):
#             result.append(path[:])
#             return

#         path.append((row, col))
#         if row<x:
#             explore(path, row+1, col)
#         if col<y:
#             explore(path, row, col+1)
#         path.pop()

#     explore([], 0, 0)
#     return result


# alll = all_paths([[0, 0, 1],
#           [1, 0, 0],
#           [1, 1, 0]])

# for path in alll:
#     print(path)