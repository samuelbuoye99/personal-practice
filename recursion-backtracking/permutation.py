def permutation(items: list):
    result = []

    def explore(path: list):
        if len(path) == len(items):
            result.append(path[:])
            return

        for i in range(len(items)):
            if items[i] in path:
                continue
            path.append(items[i])
            explore(path)
            path.pop()

    explore([])
    return result


print(permutation([1, 2, 3]))