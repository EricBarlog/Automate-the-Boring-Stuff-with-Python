# Chapter 7 Examples

import re

heroRegex = re.compile(r'Batman|Tina Fey')
mo1 = heroRegex.search('Batman and Tina Fey')
print(mo1.group())

mo2 = heroRegex.search('Tina Fey and Batman')
print(mo2.group())

# Describes how many instances of value to find
haRegex = re.compile(r'(Ha){3}')
mo3 = haRegex.search('HaHaHa')
print(mo3.group())
mo4 = haRegex.search('Ha')
print(mo4)

# Greedy string example
greedyHaRegex = re.compile(r'(Ha){3,5}')
mo5 = greedyHaRegex.search('HaHaHaHaHa')
print(mo5.group())

# Non greedy string examples
nongreedyHaRegex = re.compile(r'(Ha){3,5}?')
mo6 = nongreedyHaRegex.search('HaHaHaHaHa')
print(mo6.group())

# Findall Regex - finds all instances of that pattern
phoneNumberRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo7 = phoneNumberRegex.findall('Cell: 515-555-9999 Work: 212-555-0000')
print(mo7)

# Different class files examples
xmasRegex = re.compile(r'\d+\s\w+')
m08 = xmasRegex.findall('12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge')
print(m08)

# Vowel Regex - define own list of things to be found
vowelRegex = re.compile(r'[aeiouAEIOU]')
mo9 = vowelRegex.findall('Robocop eats baby food. BABY FOOD.')
print(mo9)
