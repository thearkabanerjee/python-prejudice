# an interesting cypher - Strings

apha = "abcdefghijklmnopqrstuvwxyz"
print (apha[0])


name = "arka"

# expected printing of bslb

for char in name:
    shifted = ''.join(chr(ord(char) + 1) for char in name)
print (shifted)
