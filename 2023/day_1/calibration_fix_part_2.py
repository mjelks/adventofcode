'''
  - open file
  - scan each row ->
    - put lines into array
    - explode string based on one,two,three,etc. + ints 1,2,3 ...
  - if no digits (skip?)
  - if only 1 digit, double it
  - take first digit, then last digit, concat to make new digit
  - finally sum up all digits
'''

import re

digits = {
  "one": 1,
  "two": 2,
  "three": 3,
  "four": 4,
  "five": 5,
  "six": 6,
  "seven": 7,
  "eight": 8,
  "nine": 9
}

def is_int_try(str):
    try:
        result = digits[str] if digits.get(str) else float(str)
        return int(result)
    except ValueError:
        return 0


try:
    with open('input.txt') as f:
      lines = f.read().splitlines()
except FileNotFoundError:
    print("Please check the path.")

# this subtotal array is just used for sanity checking to we can confirm (can be removed later)
subtotal = []
total = 0

for text_string in lines:
  temp_holder = [0, 0]
  # fix for oneight ===> one,eight && twone 
  text_string = re.sub(r'oneight', 'oneeight', text_string)
  text_string = re.sub(r'twone', 'twoone', text_string)
  text_string = re.sub(r'eightwo', 'eighttwo', text_string)
  # text_string = re.sub(r'fiveight', 'fiveeight', text_string)
  # text_string = re.sub(r'threeight', 'threeeight', text_string)
  regex = "(\d|one|two|three|four|five|six|seven|eight|nine)"
  string_chunks = re.split(regex, text_string)
  
  for value in string_chunks:
    int_value = is_int_try(value)
    if int_value > 0: 
      if temp_holder[0] > 0:
        temp_holder[1] = int_value
      else: 
        temp_holder[0] = int_value

  
  if temp_holder[1] == 0  :
    temp_holder[1] = temp_holder[0]
  
  # print(f"{idx}: {temp_holder}")
  
  # concat the ints back to strings ...
  line_value = str(temp_holder[0]) + str(temp_holder[1])
  # print(f"{idx}: {line_value}")
  # subtotal.append(line_value)
  
  # now we can add to total by parsing the int again
  total += int(line_value)

print(total)
