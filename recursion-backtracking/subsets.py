def subset(nums):
    result = []

    def explore(start, path):
        result.append(path[:])

        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[i-1]:
                continue
            path.append(nums[i])
            explore(i+1, path)
            path.pop()

    explore(0, [])
    return result

print(subset([1, 1, 2]))