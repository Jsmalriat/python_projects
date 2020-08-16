# __author__ = Jonah Malriat
# __contact__ = tuf73590@temple.edu
# __date__ = 10/25/2019
# __descript__ = This program will work as a password checker. It will allow the user to input a password on two occasions to
#     attempt to create a password. These passwords must agree with each other and must meet all specifications.

def greeting():
  print('''
----- Welcome to Password Checker! -----
  ''')

def main():
  greeting()
  pass_1 = input('''Enter your password
  =>  ''')
  pass_2 = input('''Retype your password
  =>  ''')
  do_they_match(pass_1, pass_2)
  result = password_is_valid(pass_1)
  congrats(result)

def do_they_match(pass_1, pass_2):
  if pass_1 != pass_2:
    print('These passwords do not match. Try again!')
    main()

def password_is_valid(password): # Must return boolean value if password meets all requirements.
  param_1 = at_least_eight(password)
  param_2 = no_special_start(password)
  param_3 = cont_a_letter(password)
  param_4 = cont_a_number(password)
  param_5 = cont_a_symbol(password)
  param_6 = no_spaces(password)
  param_7 = no_threepeats(password)
  if param_1 and param_2 and param_3 and param_4 and param_5 and param_6 and param_7:
    return True
  else:
    return False

def at_least_eight(password):
  if len(password) < 8:
    print('Password must be at least 8 characters.')
    return False
  elif len(password) >= 8:
    return True

def cont_a_letter(password):
  for x in password:
    if x.isalpha():
      return True
  else:
    print('Passwords must contain a letter.')
    return False

def cont_a_number(password):
  for x in password:
    if x.isnumeric():
      return True
  else:
    print('Password must contain a number.')
    return False

def cont_a_symbol(password):
  if password.isalnum():
    print('Password must contain a special character.')
    return False
  else:
    return True

def no_spaces(password):
  if ' ' in password:
    print('Password cannot contain any spaces or dashes.')
    return False
  elif '-' in password:
    print("Password cannot contain any spaces or dashes.")
    return False
  else:
    return True

def no_special_start(password):
  if password.startswith('&'):
    print("Password cannot start with the '&' symbol.")
    return False
  elif password.startswith('*'):
    print("Password cannot start with the '*' symbol.")
    return False
  else:
    return True

def no_threepeats(password):
  for i in range(len(password)):
    if password[i] == password[i - 1] == password[i + 1]:
      print('Password cannot contain 3 of the same character in a row.')
      return False
  else:
    return True 

def congrats(result):
  if result == False:
    print ('''^ Read the above errors and try again. ^
    ''')
    main()
  else:
    print ('Congratulations, your password has been created!')


if __name__ == '__main__':
  main()