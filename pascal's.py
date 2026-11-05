def pascal(num):
    result = [[1]*i for i in range(1, num+1)]

    for i in range(2, len(result)):
        x = len(result[i])//2 if len(result[i])%2==0 else (len(result[i])//2)+1
        for j in range(1, x):
            result[i][j] = result[i-1][j-1]+result[i-1][j]
            result[i][-j-1] = result[i][j]
    return result

def generate(numRows):
    result = [[1]*i for i in range(1, numRows+1)]

    for i in range(2, len(result)):
        x = len(result[i])//2 if not len(result[i])%2 else (len(result[i])//2)+1
        for j in range(1, x):
            result[i][j] = result[i-1][j-1] + result[i-1][j]
            if i%2==0 and j==x-1:
                continue
            result[i][-j-1] = result[i][j]
    return result

for level in pascal(10):
    print(level)

for level in generate(5):
    print(level)