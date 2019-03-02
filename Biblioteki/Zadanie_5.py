import re
import struct
import json

with open(r"input.txt", 'r') as f:
    s = f.read()
    print(s)

print(re.findall(r'\d{2}-\d{3}', s))
# print(re.findall(r'\w+', s))  wyprintowanie wszystkich napisow
print(re.findall(r'[\w\-+.]+@[\w\-.]+', s))
print(re.findall(r'.\d\d \w\w\w \d\d\d\d', s))


# pythonchallenge.com

# from string import ascii_letters
# ascii_lowercase