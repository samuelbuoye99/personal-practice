def num_decoding(s):
    pass

def encode(char):
    return (ord(char)-ord("A")+1)

def decode(num):
    return chr(ord("A")+num-1)

while True:
    char = int(input("Character: "))
    print(decode(char))