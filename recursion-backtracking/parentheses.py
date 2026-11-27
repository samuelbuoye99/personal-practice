def generate_parens(n: int):
    result = []

    def explore(path: list[str], open: int, close: int):
        if len(path) == n*2:
            result.append("".join(path))
            return

        if open<n:
            path.append("(")
            explore(path, open+1, close)
            path.pop()

        if close<open:
            path.append(")")
            explore(path, open, close+1)
            path.pop()

    explore([], 0, 0)
    return result

print(generate_parens(3))