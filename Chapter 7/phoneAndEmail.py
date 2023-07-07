# phoneAndEmail - Finds phone numbers and email addresses on the clipboard

import pyperclip, re

### Phone Regex
# need to mimic (DDD)-DDD-DDDD ext. DDD

phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?       # Area code
    (\s|-|\.)                # Space seperator
    (\d{3})                  # Firsts phone digits
    (\s|-|\.)                # Space seperator
    (\d{4})                  # Four digits
    (/s*(ext|x|ext.)\s*(\d{2,5}))?
)''', re.VERBOSE)

### Email Regex
# format dddddddd@dddddd.ddd

emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+       # Possible username characters
    @                       # @ symbol
    [a-zA-Z0-9.-]+          # Possible domain name
    (\.[a-zA-Z]{2,4})       # Dot-something
)''', re.VERBOSE)

# Search for matches on the clipboard
text = str(pyperclip.paste())

matches = []
for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phoneNum += ' x' +groups[8]
    matches.append(phoneNum)
for groups in emailRegex.findall(text):
    matches.append(groups[0])

# Send matches to the clipboard
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found.')