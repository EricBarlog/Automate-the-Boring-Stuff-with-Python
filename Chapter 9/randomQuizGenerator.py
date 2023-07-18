# Ch.9 Project Randomized Quiz Files Project

import random

# Quiz data - State then Capitol in dictionary 
capitals = {'Alabahma': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix', 'Arkansas': 'Little Rock', 'California': 'Sacremento', 'Colorado': 'Denver', 'Conneticut': 'Hartford', 
            'Delaware': 'Dover', 'Florida': 'Tallahassee', 'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois': 'Springfield', 'Indiana': 'Idianaopolis', 'Iowa': 'Des Moines',
            'Kansas': 'Topeka', 'Kentucky': 'Frankfort', 'Lousiana': 'Baton Rouge', 'Maine': 'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan': 'Lansing', 'Minnesota': 'Helena',
            'Nebraska': 'Lincoln', 'Neveda': 'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
            'North Dakota': 'Bismark', 'Ohio': 'Columbud', 'Oklahoma': 'Oklahoma City', 'Oregon': 'Salem', 'Pennslyvania': 'Harrisburg', 'Rhode Island': 'Providence', 'South Carolina': 'Columbia',
            'South Dakota': 'Pierre', 'Tennesse': 'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont': 'Monpelier', 'Virgnia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston', 
            'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

# Quiz Generation
for quizNum in range(35):
    # TODO: Create Quiz and asnwer keys
    # Create the Quiz and the answer keys for each one
    quizFile = open(f'captalsquiz{quizNum + 1}.txt', 'w')
    answerKeyFile = open(f'captalsquiz_answers{quizNum + 1}.txt', 'w')

    # TODO: Write out the header for the quiz
    # Header for each quiz
    quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')
    quizFile.write((' ' * 20) + f'State Capitals Quiz (Form{quizNum + 1})')
    quizFile.write('\n\n')

    # TODO: Shuffle the order of the states
    # Shuffle order of states
    states = list(capitals.keys())
    random.shuffle(states)

    # TODO: Loop through all 50 states, making a question for each state
    for questionNum in range(50):
        # Get right and wrong answers
        correctAnswer = capitals[states[questionNum]]
        wrongAnswers = list(capitals.values())
        del wrongAnswers[wrongAnswers.index(correctAnswer)]
        wrongAnswers = random.sample(wrongAnswers, 3)
        answerOptions = wrongAnswers + [correctAnswer]
        random.shuffle(answerOptions)

        # Create questions and Answers for each problem
        quizFile.write(f'{questionNum + 1}. What is the capital of {states[questionNum]}?\n')
        for answersA2D in range(4):
            quizFile.write(f"   {'ABCD'[answersA2D]}. { answerOptions[answersA2D]}\n")
        quizFile.write('\n')

        # Create answer key for the file
        answerKeyFile.write(f"{questionNum + 1}. {'ABCD'[answerOptions.index(correctAnswer)]}")
        quizFile.close()
        answerKeyFile.close()
