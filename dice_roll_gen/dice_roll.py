# __author__ = Jonah Malriat
# __contact__ = tuf73590@gmail.com
# __date__ = 10/11/2019
# __descript__ = This program takes user-input to determine the amount of times two dice are rolled.
#   The program then adds these two dice rolls for every time they were rolled and outputs how many
#   times each number 2 - 12 was rolled and the percentage it was rolled. It then compares this percentage
#   to the probability and finds the difference between the two values.

import random

def greeting():
  print('=> Welcome to the random dice-roll generator!')

def num_iterations():
  iter = input('=> How many times would you like to roll the dice? ')
  return iter

def first_roll():
  first_roll = random.randint(1, 6)
  return first_roll

def second_roll():
  second_roll = random.randint(1, 6)
  return second_roll

def roller(iter):
  roll_list = []
  for i in range(0, iter):
    roll_list.append(first_roll() + second_roll())
  return roll_list

def num_of_value(roll_list, num):
  x = 0
  for i in roll_list:
    if i == num:
      x += 1
  return x

def perc_of_value(roll_list, num):
  y = 0
  x = num_of_value(roll_list, num)
  for i in roll_list:
    y += 1
  x /= y
  x *= 100
  return round(x, 2)

def expected_prob(num):
  if num == 2:
    x = (1 / 36) * 100
  elif num == 3:
    x = (1 / 18) * 100
  elif num == 4:
    x = (1 / 12) * 100
  elif num == 5:
    x = (1 / 9) * 100
  elif num == 6:
    x = (5 / 36) * 100
  elif num == 7:
    x = (1 / 6) * 100
  elif num == 8:
    x = (5 / 36) * 100
  elif num == 9:
    x = (1 / 9) * 100
  elif num == 10:
    x = (1 / 12) * 100
  elif num == 11:
    x = (1 / 18) * 100
  elif num == 12:
    x = (1 / 36) * 100
  return round(x, 2)

def diff_in_prob(roll_list, x):
  x = abs(perc_of_value(roll_list, x) - expected_prob(x))
  return round(x, 2)

def print_iter(iter):
  print(f"Number of iterations = {iter}")

def print_key(a, b, c, d, e):
  print('{:^14}'.format(a), '{:^14}'.format(b), '{:^14}'.format(c), '{:^14}'.format(d), '{:^14}'.format(e))

def print_table(a, b, c, d, e):
  print('{:^14}'.format(a), '{:^14}'.format(b), '{:^14}'.format(f"{c}%"), '{:^14}'.format(f"{d}%"), '{:^14}'.format(f"{e}%"))

def table_maker(roll_list):
  x = 1
  while x < 12:
    x += 1
    print_table(f"{x}", num_of_value(roll_list, x), perc_of_value(roll_list, x), expected_prob(x), diff_in_prob(roll_list, x))

def main():
  greeting()
  iter = int(num_iterations())
  roll_list = roller(iter)
  print_iter(iter)
  print_key('Number', 'Times Rolled', 'Percentage', 'Expected', 'Difference')
  table_maker(roll_list)

if __name__ == '__main__':
  main()