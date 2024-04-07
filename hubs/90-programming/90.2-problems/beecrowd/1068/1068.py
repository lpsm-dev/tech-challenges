# -*- coding: utf-8 -*-

for element in range(0, 10000):
  try:
    expression = input()
    values = [char for char in expression if char == '(' or char == ')']
    if values[0] == ')': print('incorrect')
    else:
      count, correct = 0, True
      for value in values:
        if value == '(':
          count += 1
        elif value == ')':
          count -= 1
        if count < 0:
          correct = False
          break
      if count != 0:
        correct = False
      if correct:
        print('correct')
      else:
        print('incorrect')
  except EOFError:
    break
