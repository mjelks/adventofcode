'''
  - set cube config number limits
  - open input file
  - loop through each line, 
    - remove line counter + colon + space (use our own index instead)
    - set cube_config per line, update min number of cubes as we iterate
    - at the end of the parsing, make note of the three values
    - multiply the three values to get our power, append to subtotal array
    - total up the subtotal for the final amt


'''

import re
from functools import reduce

# this subtotal array is just used for sanity checking to we can confirm (can be removed later)
subtotal = []
total = 0

def check_cube_config(cube_config, color, amount):
  amount = int(amount)
  if amount > cube_config[color]:
    cube_config[color] = amount
  
  return cube_config  

def check_cube_vals(games):
  cube_config = {
    'red': 0,
    'green': 0,
    'blue': 0
  }
  games =  re.split(';', text_string)

  # 3 blue, 4 red, 11 green
  for gameset in games:  
    # strip whitespaces
    # now we have '4 green', '2 blue'
    gameset = [x.strip() for x in gameset.split(',')]
    for cube_pull in gameset:
      vals = [x.strip() for x in cube_pull.split(' ')]
      cube_config = check_cube_config(cube_config, vals[1], vals[0])

  # once we get the high vals for the cube config, multiply the three vals to get our power
  return reduce(lambda x, y: x*y, cube_config.values())



try:
    with open('input.txt') as f:
      lines = f.read().splitlines()
except FileNotFoundError:
    print("Please check the path.")

for text_string in lines:
  text_string = re.sub(r'Game \d+:\s*', '', text_string)
  
  games =  re.split(';', text_string)
  subtotal = check_cube_vals(games)
  # print(subtotal)
  total += subtotal
  
  
print(total)