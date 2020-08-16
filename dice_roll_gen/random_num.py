# __author__ = Jonah Malriat
# __contact__ = tuf73590@gmail.com
# __date__ = 10/11/2019
# __descript__ = This program takes user-input to determine the amount of times a number from 2 - 12 is generated.
#   The program then outputs the amount of times a number was generated, how many times each number from 2 - 12
#   was landed on, and the percentage. It then compares this percentage to the probability and finds the difference 
#   between the two values.


import random

def greeting():
  print('=> Welcome! This program will randomly generate a number from 2 - 12 for the amount of times you select.')

def num_iterations():
  iter = input('=> How many times would you like this program to generate a number? ')
  return iter

def roll_it():
  roll_it = random.randint(2, 12)
  return roll_it

def roller(iter):
  roll_list = []
  for i in range(0, iter):
    roll_list.append(roll_it())
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
  return round(x, 1)

def expected_prob(num):
  if num:
    x = (1 / 11) * 100
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
  print_key('Number', 'Times Generated', 'Percentage', 'Expected', 'Difference')
  table_maker(roll_list)

if __name__ == '__main__':
  main()