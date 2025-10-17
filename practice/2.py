# consider a python program which takes a statement (containing both capital and small letters, spaces and punctuation)
#and prints the number of vowels

# snippet 1 

sentence = input()

count = 0

vowels = set("aeiouAEIOU")

for char in sentence:
    if char in vowels:
        count += 1
    
print (count) # works very well written code

# snippet -2 

sentence = input ()

count = 0 

for char in sentence.lower():
    if char in ['a', 'e', 'i', 'o', 'u']:
        count += 1

print (count) # works both yayy