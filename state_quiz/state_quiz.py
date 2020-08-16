# __author__ = Jonah Malriat
# __contact__ = tuf73590@temple.edu
# __date__ = 10/25/2019
# __descript__ = This program will store and recall the names of all 50 states and their respective captials.
#   The program will then quiz the user on either capitals or states according to input and tell the user whether they
#   are correct or incorrect. The program will then ask if they would like to play again.

import random

def greeting():
  print('''
---Welcome to the US states and capitals quiz!---''')

def s_or_c():
  x = 0
  while x == 0:
    decision = input('''Would you like to be quizzed on states or capitals? (enter "S" for states or "C" for capitals)
=> ''')
    decision = decision.lower()
    if decision == 's':
      return 0
      x += 1
    elif decision == 'c':
      return 1
      x += 1
    elif decision != 's' or decision != 'c':
      print("I'm sorry that's not a valid input.")
      x = 0

def main():
    greeting()
    s_list = state_list()
    c_list = captial_list()
    decision = s_or_c()
    which_quiz(decision, s_list, c_list)

def state_list():
  state_caps = open("capitals.txt").read().splitlines()
  state_list = []
  cap_list = []
  index = 0
  for i in state_caps:
    if index % 2 != 0:
      cap_list.append(i)
      index += 1
    else:
      state_list.append(i)
      index += 1
  return state_list

def captial_list():
  state_caps = open("capitals.txt").read().splitlines()
  state_list = []
  cap_list = []
  index = 0
  for i in state_caps:
    if index % 2 != 0:
      cap_list.append(i)
      index += 1
    else:
      state_list.append(i)
      index += 1
  return cap_list

def which_quiz(decision, s_list, c_list):
  if decision == 0:
    print('You have chosen the state quiz! You will be given a capital, type the matching state.')
    state_quiz(s_list, c_list)
  elif decision == 1:
    print('You have chosen the capital quiz! You will be given a state, type that states capital.')
    caps_quiz(s_list, c_list)

def state_quiz(s_list, c_list):
  r = True
  while r == True:
    capital = random.choice(c_list)
    state = input(f"""What state does {capital} belong to?
=> """).title()
    state_correct(state, capital, s_list, c_list)
    r = play_again()

def caps_quiz(s_list, c_list):
  r = True
  while r == True:
    state = random.choice(s_list)
    capital = input(f"""What is the capital of {state}?
=> """).title()
    capital_correct(state, capital, s_list, c_list)
    r = play_again()

def capital_correct(state, capital, s_list, c_list):
  i = s_list.index(state)
  if capital == c_list[i]:
    print('Correct!')
  else:
    print('Incorrect!')

def state_correct(state, capital, s_list, c_list):
  i = c_list.index(capital)
  if state == s_list[i]:
    print('Correct!')
  else:
    print('Incorrect!')

def play_again():
  y_or_n = input('''Would you like to play again? (type "yes" to play again, type "no" or any other input to end.)
=> ''')
  if y_or_n.lower() == 'yes':
    return True
  else:
    print('Terminated')
    return False

if __name__ == '__main__':
  main()