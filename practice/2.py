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

