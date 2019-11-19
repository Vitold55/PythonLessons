# Regular expressions
import re

s = 'Lorem ipsum dolor test amet, 98 adipiscing elit, sed do 555 eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'
pattern = r'test'

# search method
search_res = re.search(pattern, s, flags=re.I)
print(search_res, search_res.span())

# match method
match = re.match(pattern, s)
print(match)

# findall method
pattern3 = r'\d{1,3}'
finded = re.findall(pattern3, s)
print(finded)

# split method
pattern4 = r',\s'
split = re.split(pattern4, s, flags=re.IGNORECASE | re.MULTILINE)
print(split)