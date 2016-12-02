import re

a = "I can not learn code"
b = "not"
# first senario
count = sum(1 for _ in re.finditer(r'\b%s\b' % re.escape(b), a))
print(count)
c = a.replace( b , '')
print(c)
