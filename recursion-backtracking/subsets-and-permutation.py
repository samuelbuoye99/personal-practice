def subsets(nums):
    result = []

    def explore(start, path):
        result.append(path[:])

        for i in range(start, len(nums)):
            path.append(nums[i])
            explore(i+1, path)
            path.pop()

    explore(0, [])
    return result

def permutation(nums):
    result = []

    def explore(path):
        if len(path) == len(nums):
            result.append(path[:])
            return

        for num in nums:
            if num in path:
                continue
            path.append(num)
            explore(path)
            path.pop()

    explore([])
    return result

# print(subsets([1, 2, 3]))
print(permutation([1, 2, 3]))