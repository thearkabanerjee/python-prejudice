# # consider the following code:

# text = ">>> Hello world <<<"

# to_strip = 'o'

# A = text.strip(to_strip)
# print (A)

# B = text.lstrip(to_strip)

# print (B)


# C = text.strip()
# print (C)

# # what i learnt :
# """
# strip(argument) -> strips out that from the sides of the string 
# lstrip (argument) -> strips from the left side
# rstrip (argument) -> strips form the right side of the string

# """


# good example
a = "ohelloworldo"
o = "o"
astrip = a.strip(o)

print (astrip)