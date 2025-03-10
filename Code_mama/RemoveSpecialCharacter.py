import re

def remove_special_characters(s):
    return re.sub(r'[^a-zA-Z0-9 ]', '', s)

s = input()
print(remove_special_characters(s))
