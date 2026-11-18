def letter_case(s):
    result = []
    def explore(start, path):
        if len(path) == len(s):
            result.append("".join(path))
            return

        for i in range(start, len(s)):
            if s[i].isalpha():
                path.append(s[i].lower())
                explore(i+1, path)
                path.pop()
                path.append(s[i].upper())
                explore(i+1, path)
                path.pop()
            else:
                path.append(s[i])
                explore(i+1, path)
                path.pop()
    explore(0, [])
    return result

print(letter_case("a1b2"))