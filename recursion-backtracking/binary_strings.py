def binary_strings(n):
    result = []
    def explore(path, nums):
        if len(path) == n:
            result.append("".join(path))
            return

        for num in nums:
            path.append(num)
            explore(path, nums)
            path.pop()
    explore([], "01")
    return result


print(binary_strings(3))