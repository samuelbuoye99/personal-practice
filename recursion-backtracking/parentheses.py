result = []

def generate(path, open_count, close_count, n):
    if len(path) == 2 * n:
        result.append("".join(path))
        return

    if open_count<n:
        path.append("(")
        generate(path, open_count+1, close_count, n)
        path.pop()

    if close_count<open_count:
        path.append(")")
        generate(path, open_count, close_count+1, n)
        path.pop()

generate([], 0, 0, 3)
print(result)