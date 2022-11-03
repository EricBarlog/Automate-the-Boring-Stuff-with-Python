# Python Book 
# Saying Hello World and asking user's name

print('Hello World!')
print('What is your name?')

myName = input()        # Ask name
print('It is good to meet you ' + myName + '!')
lenAge = len(myName)
print('The length of your name is ' + str(lenAge) + ' letters.')

print('What is your age?')      # Ask age
myAge = input()
print('You will be ' + str(int(myAge) + 1) + ' in a year!')