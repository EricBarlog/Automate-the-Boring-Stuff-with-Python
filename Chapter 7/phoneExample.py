# Regex Example - Phone Number

import re

phoneNumberRegex = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')
mo = phoneNumberRegex.search('My number is (415) 555-4242.')

areaCode, mainNumber = mo.groups()

print(mo.group(1))
print(mo.group(2))
print(areaCode)
print(mainNumber)
print(mo.group())