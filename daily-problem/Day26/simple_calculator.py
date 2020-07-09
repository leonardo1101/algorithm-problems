'''
Probleam: Given a mathematical expression with just single digits, plus signs,
negative signs, and brackets, evaluate the expression. Assume the expression is
properly formed.

Example:
Input: - ( 3 + ( 2 - 1 ) )
Output: -4
'''
def eval(expression):
  exp_len = len(expression)
  char_digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
  digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
  stack = []
  operation = ''
  number1 = 0
  number2 = 0

  for i in range(exp_len):
    caractere = expression[i]

    if caractere == ')':
      number2 = stack.pop()
      operation = stack.pop()
      number1 = stack.pop()

      if number1 in digits:
        if operation == '+':
          stack.append(number1 + number2)
        else:
          stack.append(number1 - number2)
      else:
        stack.append(number1)
        if operation == '-':
          stack.append(-number2)
    else:
      if caractere != '(' and caractere != ' ' :
        if caractere in char_digits:
          stack.append(int(caractere))
        else:
          stack.append(caractere)

  while len(stack) != 1:
      number2 = stack.pop()
      operation = stack.pop()
      number1 = ''
      if stack:
        number1 = stack.pop()

      if number1 in digits:
        if operation == '+':
          stack.append(number1 + number2)
        else:
          stack.append(number1 - number2)
      else:
        if number1 != '':
          stack.append(number1)
        if operation == '-':
          stack.append(-number2)
  return stack[0]

print(eval('- (3 + ( 2 - 1 ) + 2 )'))
