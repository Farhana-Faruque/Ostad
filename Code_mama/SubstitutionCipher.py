def caesar_cipher(s, n):
    result = ""
    
    for char in s:
        if char.isalpha():
            shift = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - shift + n) % 26 + shift)
        else:
            result += char 

    return result

inputs = input().split()
s = inputs[0]
n = int(inputs[1])

print(caesar_cipher(s, n))
