def digitsum(n):
    if n < 10:
        return n
    return (n%10)+digitsum(n//10)

num = int(input("Number: "))
print(digitsum(num))