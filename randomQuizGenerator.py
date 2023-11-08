#randomQuizGenerator.py
#Generates 35 quizes with 50 questions (the U.S state capitals).
#Every question has 4 possible answers (A, B, C, D) with 1 being correct.
#Generates a quiz file for each quiz, and a second file with the answer keys.
import random
#Step 1: Data
capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
   'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
   'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
   'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
   'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
   'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
   'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
   'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
   'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
   'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe', 'New York': 'Albany',
   'North Carolina': 'Raleigh', 'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
   'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
   'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
   'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
   'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}
#Step 2: Generate a random quiz with 50 questions
quiz = []
#quiz wordt een random lijst van 50 staten waarvan de hoofdstad gevraagd wordt.
for i in range (0,50):
  newState = random.choice(list(capitals.keys()))
  #capitals.keys() method geeft geen lijst weer, het geeft een speciale value die geen lijst is.
  #We kunnen er als volgt wel een lijst van maken: list(capitals.keys()). Dit maakt een lijst van de keys van de capitals dictionairy, dus van alle staten.
  #random choice neemt een random objec deze lijst, dus het neemt een random staat.
  if newState in quiz:
    continue
  else:
    quiz.append(newState)
return quiz
  #correctAnswer = capitals[quiz[i]]