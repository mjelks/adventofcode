'''
  - set cube config number limits
  - open input file
  - loop through each line, 
    - remove line counter + colon + space (use our own index instead)
    - split on the semicolon
    - parse the cube count based on hash limits
    - append index + 1 value to ID counter summation 


'''

import re

cube_config = {
  'red': 12,
  'green': 13,
  'blue': 14
}

# this subtotal array is just used for sanity checking to we can confirm (can be removed later)
subtotal = []
total = 0

def check_cube_config(color, amount):
  if int(amount) > cube_config[color]:
    return False
    
  # return false if amount > cube_config.get(color)

def check_cube_vals(games):
  # 3 blue, 4 red, 11 green
  for gameset in games:  
    # strip whitespaces
    # now we have '4 green', '2 blue'
    gameset = [x.strip() for x in gameset.split(',')]
    for cube_pull in gameset:
      vals = [x.strip() for x in cube_pull.split(' ')]
      result = check_cube_config(vals[1], vals[0])
      # print(result)
      if result == False:
        return False

  return True

try:
    with open('input.txt') as f:
      lines = f.read().splitlines()
except FileNotFoundError:
    print("Please check the path.")

for idx, text_string in enumerate(lines):
# for text_string in lines:
  text_string = re.sub(r'Game \d+:\s*', '', text_string)
  games =  re.split(';', text_string)

  result = check_cube_vals(games)
  # print(result)
  if result: 
    current_game_index = idx+1
    subtotal.append(current_game_index)
    total += current_game_index
  
  
  

  
  
  
  
print(subtotal)
print(total)