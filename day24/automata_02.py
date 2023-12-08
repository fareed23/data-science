states = ['q0', 'q1', 'q2'] 

# DFA 2
def accept_re2(input_str):

  current_state = 'q0'
  
  for symbol in input_str:
    if current_state == 'q0':
      if symbol == '1':
        current_state = 'q1'
      else:
        return False

    elif current_state == 'q1':
      if symbol == '0':
        current_state = 'q2'
      else: 
        return False

    elif current_state == 'q2':
      if symbol in ['0', '1']:
        current_state = 'q2'
      else:
        return False

  return current_state == 'q2'

input_str = input("Enter input string: ")
if accept_re2(input_str):
  print("Input string accepted")
else:
  print("Input string rejected")