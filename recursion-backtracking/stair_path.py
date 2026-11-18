def stair_path(n: int) -> list[list]:
    result = []
    def explore(start: int, path: list[int]) -> None:
        if sum(path)==n:
            result.append(path[:])
            return

        for num in range(start, 4):
            if num+sum(path)>n:
                continue
            path.append(num)
            explore(num, path)
            path.pop()

    explore(1, [])
    return result

print(stair_path(4))