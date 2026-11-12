def count_ways(amount, coins):
    result = []

    def explore(start, path):
        if sum(path) == amount:
            result.append(path[:])
            return

        for i in range(start, len(coins)):
            if coins[i] + sum(path) > amount:
                continue
            path.append(coins[i])
            explore(start+i, path)
            path.pop()

    explore(0, [])
    return (result)


print(count_ways(10, [2, 5, 3, 6]))