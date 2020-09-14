import re

x = "abracadabra_ a a9aad aaaaaaaaaaaad"
y = re.findall("(a\w)", x)
print(y)

y = re.findall("(a+d)", x)
print(y)

x = "Ora este 14:22. Mai sunt 20 de mionute pana la ora 14:42."
y = re.search("([0-2]*[0-9]:[0-5][0-9])", x)

print(y.groups())
print(y.span())