result = []
def find(path, nums, start, total):
    if sum(path) == total:
        result.append(path[:])

    for i in range(start, len(nums)):
        path.append(nums[i])
        find(path, nums, i+1, total)
        path.pop()

result = []

def find(path, nums, start, total):
    if total == 5:
        result.append(path[:])
        return

    for i in range(start, len(nums)):
        if total + nums[i] > 5:      # prune: too big already
            continue
        path.append(nums[i])
        find(path, nums, i, total + nums[i])
        path.pop()

find([], [2, 2, 1], 0, 0)
print(result)

# find([], [1, 2, 3, 4], 0, 5)
# print(result)
