import re

s = "Ala ma kota! Kot ma Ale. Kot lubi mleko. Nie lubi ryb."

print(re.findall('lubi', s))
print(re.findall('lubi .', s))
print(re.findall('... ma', s))
print(re.findall('.{3} ma', s))
print(re.findall('\w', s))
print(re.findall('\w*', s))
print(re.findall('\w+', s))
print(re.findall(r'\w+', s))
print(re.findall(r'\w+\t', s))
print(re.findall(r'[A-Z].*\.', s))
print(re.findall(r'[A-Z].*?\.', s))
print(re.findall(r'[A-Z].*?[\.\!]', s))