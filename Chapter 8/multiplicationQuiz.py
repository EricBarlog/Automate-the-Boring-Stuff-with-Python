# Multiplication Quiz

import pyinputplus as pyip, time, random

numberOfQuestions = 10
correctAnswers = 0

for questionNumber in range(numberOfQuestions):
    # pick two random numbers
    num1 =  random.randint(0, 9)
    num2 = random.randint(0, 9)

    prompt = '#%s: %s x %s = ' % (questionNumber, num1, num2)

    try:
        pyip.inputStr(prompt, allowRegexes=['^%s$' % (num1 * num2)], blockRegexes=[('.*', 'Incorrect!')], timeout=8, limit=3)
    except pyip.TimeoutException:
        print('Out of Time!')
    except pyip.RetryLimitException:
        print('Out of Tries!')
    else:
        print('Correct!')
        correctAnswers += 1

        time.sleep(1)
    print('Score: %s / %s' % (correctAnswers, numberOfQuestions))
