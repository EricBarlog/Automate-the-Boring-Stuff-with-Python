# Busy idiot example

import pyinputplus as pyip

while True:
    prompt = ('Want to know how to keep an idiot busy? ')
    responce = pyip.inputYesNo(prompt)
    if responce == 'no':
        break

print('Thanks, have a nice day.')