'''
  - open file
  - scan each row ->
    - put lines into array
    - explode string into chars
  - if no digits (skip?)
  - if only 1 digit, double it
  - take first digit, then last digit, concat to make new digit
  - finally sum up all digits
'''

def is_int_try(str):
    try:
        result = float(str)
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
  chars = list(text_string) # split the string into chars
  
  for char in chars:
    int_value = is_int_try(char)
    if int_value > 0: 
      if temp_holder[0] > 0:
        temp_holder[1] = int_value
      else: 
        temp_holder[0] = int_value

  
  if temp_holder[1] == 0  :
    temp_holder[1] = temp_holder[0]
  
  # concat the ints back to strings ...
  line_value = str(temp_holder[0]) + str(temp_holder[1])
  
  subtotal.append(line_value)
  # now we can add to total by parsing the int again
  total += int(line_value)

print(subtotal)  
print(total)

