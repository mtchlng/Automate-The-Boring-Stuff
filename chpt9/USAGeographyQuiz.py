#Making 35 random USA state capitals quizzes
#Saves each quiz and answer key to its own file
#! python3


# 1. Create 35 different quizzes
# 2. Each quiz has 50 multiple choice questions in random order
# 3. Multiple choice: 3 random wrong answers, 1 random correct answer (random order)
    # Make sure to keep track of correct answers already used!
# 4. Write the quiz to 35 text files
# 5. Write the answer keys to 35 text files
    # Altogether there will be 70 (!!) text files created

import random

capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
   'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
   'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
   'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
   'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
   'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
   'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
   'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
   'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
   'Carson City', 'New Hampshire': 'Concord', 'New Jersey':
   'Trenton', 'New Mexico': 'Santa Fe', 'New York': 'Albany',
   'North Carolina': 'Raleigh', 'North Dakota': 'Bismarck', 'Ohio': 'Columbus',
   'Oklahoma': 'Oklahoma City', 'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg',
   'Rhode Island': 'Providence', 'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
   'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
   'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia',
   'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

#createQuiz
#for i in range(35):
for i in range(1): #TESTRUN
#TODO: Create quiz file, answer file key
    quizFile = open(f'capitalsquiz{i+1}.txt', 'w')
    answerKeyFile = open(f'capitalsquiz_answers{i+1}.txt','w')
#TODO: Write quiz header
    quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')
    quizFile.write((''*20)+f'State Capitals Quiz (Form{i+1})')
    quizFile.write('\n\n')
#TODO: Shuffle order of states
    states = list(capitals.keys())
    random.shuffle(states)

#TODO: Loop through 50 states, make question for each one
    for j in range(50):
        #Correct and incorrect answers
        correctAnswer = capitals[states[j]]
        wrongAnswers = list(capitals.values())
        del wrongAnswers[wrongAnswers.index(correctAnswer)]
        wrongAnswers = random.sample(wrongAnswers, 3)
        answerOptions = wrongAnswers + [correctAnswer]
        random.shuffle(answerOptions)
        #TODO: Write question and answer options to quiz file
        quizFile.write(f'{j+1}. What is the capital of {states[j]}?\n')
        for l in range(4): quizFile.write(f"{'ABCD'[l]}.{answerOptions[l]}\n")
        quizFile.write('\n')
        #TODO: Write answer key to a file
        answerKeyFile.write(f"{j+1}.{'ABCD'[answerOptions.index(correctAnswer)]}\n")
    quizFile.close()
    answerKeyFile.close()
