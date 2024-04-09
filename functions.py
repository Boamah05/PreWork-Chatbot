def welcome_mes():
  name = input('What is you name? ')
  global age
  try:
    age = int(input(f'Nice to meet you, {name}. How old are you? '))
  except ValueError:
    print('Please enter valid age. ')
    age = int(input('How old are you? '))
  print(f'\nWelcome {name}, to the Omega Chatbot. How can I help you today?')


def display_menu():
  print("\n-_OMEGA CHATBOT_-\nWhat type of account would you like to create today?")  
  print("I. Savings Account") 
  print("II. Checking Account")   
  print("III. Money Market Account")  
  print("IV. Exit\n")


def choice():
  game = True
  global one
  one = 0
  decision = int(input('Pick 1 - 4: '))
  if decision == 1:
    one = 1
    savings()
  elif decision == 2:
    one = 2
    checking(age)
  elif decision == 3:
    one = 3
    money_market()
  elif decision == 4:
    print('Thanks for using Omega Chatbot. See you soon!')
    game = False


def savings():
  address = input('Please enter your address: ')
  contact = input('Please enter your primary contact number (XXX-XXX-XXXX): ')
  min = int(input('Please enter your minimum deposit: '))
  if min >= 20:
    verify(address, contact)
  else:
    print('Minimum deposit must be at least 20 dollar. PLease enter suffiecient value. ')
    savings()


def checking(age):
  if age >= 18:
    address = input('Please enter your address: ')
    license = input('Do you have a valid driver\'s license? (Y/N): ')
    contact = input('Please enter your primary contact number: ')
    verify(address, contact,license)
  else:
    print('You are not eligible to open a checking account. Please resume back to menu.')
    display_menu()
    choice()


def money_market():
  if age >= 18:
    address = input('Please enter your address: ')
    license = input('Do you have a valid driver\'s license? (Y/N): ')
    contact = input('Please enter your primary contact number: ')
    min = int(input('Please enter your minimum deposit: '))
    if min >= 5000:
      verify(address, contact,license)
    else:
      print('Minimum deposit must be at least 5000 dollar. PLease enter suffiecient value. ')
      money_market()
  else:
    print('You are not eligible to open a money market account. Please resume back to menu.')
    display_menu()
    choice()


def verify(address, contact, license = ''):
  print('Please verify the following')
  address_verify = input('Please enter your address: ')
  contact_verify = input('Please enter your primary contact number: ')
  if license == '':
    if one == 1:
      print('You have created your Savings Account')
    elif one == 2:
      print('You have created your Checking Account')
    elif one == 3:
      print('You have created your Money Market Account')
    display_menu()
    choice()
  else:
    license_verify = input('Do you have a valid driver\'s license? (Y/N): ')
  if address_verify == address and contact_verify == contact and license_verify == license:
    if one == 1:
      print('You have created your Savings Account')
    elif one == 2:
      print('You have created your Checking Account')
    elif one == 3:
      print('You have created your Money Market Account')
    display_menu()
    choice()
  else:
    print('Please try again.')
    verify(address, contact)
  


    