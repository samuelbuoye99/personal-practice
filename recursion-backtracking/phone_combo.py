def letter_combos(digits: str) -> list[str]:
    keys = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl",
        "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
    result = []

    def explore(path: list, start: int):
        if len(path) == len(digits):
            result.append("".join(path))
            return

        for i in range(start, len(digits)):
            letters = keys[digits[i]]
            for char in letters:
                path.append(char)
                explore(path, i+1)
                path.pop()

    explore([], 0)
    return result

print(letter_combos("79"))