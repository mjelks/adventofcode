'''
  - per row, grab the contiguous numbers along with the array index values
    - also grab any symbols and their array index values
    - create a array of hashes with structure like : 
      [
        {
          '467': [0, 1, 2],
          '114': [5, 6, 7]
        },
      ]
    - array of arrays noting the index(es) where symbols appear:
      [[], [3], [], [6], [3], [5], [], [], [3, 5], []]
    - loop through symbols, add to a new array of the key value of number if number near :
      - current_row index -1
      - current_row index +1
      - previous_row index -1, same_index, index +1
      - next_row  index -1, same_index, index +1      
'''
import re

debug = False
input_file = 'input.txt'
numberDict = []
symbolArrayIndexes = []
validNumbers = []

def populateNumberDict(text_string):
  temp = []
  for match in re.finditer(r'\d+', text_string):
  # print(f"match: {match.group()} match_start: {match.start()} match_end: {match.end()}")
  # print(f"range:??? {list(range(match.start(), match.end()))}")
    temp.append({match.group(): list(range(match.start(), match.end()))})
  numberDict.append(temp)

def populateSymbolsArray(text_string):
  temp = []
  for match in re.finditer(r'[^\d.]', text_string):
    # print(f"match: {match.group()} match_start: {match.start()} match_end: {match.end()}")
    # print(f"range:??? {range(match.start(), match.end())}")
    temp.append(match.start())
    
  symbolArrayIndexes.append(temp)

# we want to merge values of row-1, row, row+1
# then check for idx, idx -1, idx +1 
# that is a match
# lastly add key numberDict value to the validNumbers array
def checkForMatch(row_index, symbolIndex):
  valid_range = list(range(symbolIndex-1, symbolIndex+2))
  numberDictRows = list(range(row_index-1, row_index+2))
  
  if debug:
    print(f"row index: {row_index}")
    print(f"numberDictRows: {numberDictRows}")
    print(f"symbol index: {symbolIndex}")
    print(f"valid range: {valid_range}")

  # ok valid range check time : 
  for row_number in numberDictRows:
    if numberDict[row_number]:
      for idx, dictionary in enumerate(numberDict[row_number]):
        for key, values in dictionary.items():
          if any(value in valid_range for value in values):
              if debug:
                print(f"At least one value exists in the array. {key} : {values}") 
              validNumbers.append(int(key)) 
              # del numberDict[row_number][idx]
  

try:
    with open(input_file) as f:
      lines = f.read().splitlines()
except FileNotFoundError:
    print("Please check the path.")


for text_string in lines:
  
  populateNumberDict(text_string)
  populateSymbolsArray(text_string)

  # for match in re.finditer(r'\d+', text_string):
  #   # print(f"match: {match.group()} match_start: {match.start()} match_end: {match.end()}")
  #   # print(f"range:??? {list(range(match.start(), match.end()))}")
  #   temp_numbers.append({match.group(): list(range(match.start(), match.end()))})
  # numberDict.append(temp)

if debug:
  print(numberDict)  
  print("\n\n")

for row_index, symbolIndexes in enumerate(symbolArrayIndexes):
  if symbolIndexes:
    for symbolIndex in symbolIndexes:
      checkForMatch(row_index, symbolIndex) 
    
    if debug:
      print(f"where we at now with numberDict?: {numberDict}")

print(f"validNumbers: {validNumbers}")
print(f"validNumbers sum: {sum(validNumbers)}")


# 480854 is too low !
# 498559 is the correct answer (phew!)
