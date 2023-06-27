# Birthday Example
Birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4' }

while True:
    print('Enter a name: (blank to quit)')
    name = input()
    if name == '':
        break

if name in Birthdays:
    print(Birthdays[name] + ' is the burthday of ' + name)
else:
    print('I do not have information on that birthday for' + name)
    print('What is their birthday?')
    bday = input()
    Birthdays[name] = bday
    print('Birthday database updated')
