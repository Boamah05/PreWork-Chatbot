def welcome_mes():
  name = input('What is you name? ')
  try:
    age = int(input(f'Nice to meet you, {name}. How old are you? '))
  except ValueError:
    print('Please enter valid age. ')
    age = int(input('How old are you? '))
  print(f'\nWelcome {name}, to the Omega Chatbot. How can I help you today?')

def display_menu():
  print("\n-_OMEGA CHATBOT_-")  
  print("I. Option #1 ") 
  print("II. Option #2")   
  print("III. Option #3")  
  print("IV. Exit\n")

def choice():
  game = True
  decision = int(input('Pick 1 - 4: '))
  if decision == 1:
    print('y')
  elif decision == 2:
    print('yo')
  elif decision == 3:
    print('yoy')
  elif decision == 4:
    print('Thanks for using Omega Chatbot. See you soon!')
    game = False



    