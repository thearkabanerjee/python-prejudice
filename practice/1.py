# consider the following code:

text = ">>>>> Hello world <<<<"

to_strip = '><'

A = text.strip(to_strip)
print (A)

B = text.lstrip(to_strip)

print (B)


C = text.strip()
print (C)