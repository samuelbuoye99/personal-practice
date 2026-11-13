def letter_combos(digits):
    
    result = []

    def explore(start, path):
        KEYS = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl",
                "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        
        if len(path) == len(digits):
            result.append("".join(path))
            return
        
        for i in range(start, len(digits)):
            for char in KEYS[digits[i]]:
                if path and path[-1] in KEYS[digits[i]]:
                    continue
                path.append(char)
                explore(start+1, path)
                path.pop()

    explore(0, [])
    return result

print(letter_combos("23"))