# what is the output of the following code

for char in 'a1b2c3d4e5':
    if char in 'abcde':
        print('|', end = '') # there is no space between the quotes
        continue
    print(char, end = '')  # there is no space between the quotes
print('|')

# if the while loop of the below code executes, what does it terminates

x = int(input("Enter any number: "))
while(x % 5 != 0 and x % 10 != 0):
    x = int(input("Enter any number: "))
print("outside loop, the value of x is ", x)



# code 1 and code 2 will return the same value

# code 1
x = 0
x_ = 1
for i in range(10):
    x, x_ = x_, x + x_
print(x)

# code 2 
x = 0
x_ = 1
for i in range(10):
    x = x_
    x_ = x + x_
print(x)

alpha = 'abcdefghijklmnopqrstuvwxyz'
shift = 5
word = 'python'
encoded_word = ''  # there is no space between quotes
for char in word:
    shifted_index = (alpha.index(char) + shift) % 26
    encoded_char = alpha[shifted_index]
    encoded_word += encoded_char
print(encoded_word)


