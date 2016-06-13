def shiftCipher(text, k):
    cipherText = ""
    a = ord('a')
    z = ord('z')
    for i in range(len(text)):
        n = ord(text[i])
        n = (n + k % 26) #add an amount between 0 and 25
        if n > z:
            n -= 26
        c = chr(n)
        cipherText += c
    return cipherText