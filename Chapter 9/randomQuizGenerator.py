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

# Quiz Genereation
for quizNum in range(35):
    # TODO: Create Quiz and asnwer keys
    # TODO: Write out the header for the quiz
    # TODO: Shuffle the order of the states
    # TODO: Loop through all 50 states, making a question for each state