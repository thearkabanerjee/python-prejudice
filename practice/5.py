# an interesting cypher - Strings

apha = "abcdefghijklmnopqrstuvwxyz"
print (apha[0])


name = "arka"

# expected printing of bslb

# expected code might be 

name = "arkz"
shifted = ""
for c in name:
    shifted += chr(ord(c)+1)
print(shifted)  # Output: bslb

