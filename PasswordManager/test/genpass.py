import random
import array
 

MAX_LEN = 25

onPressUpper = True
onPressLower = True
onPressSymbols = True
onPressDigits = True
 

DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] 
LOCASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                     'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
                     'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                     'z']
 
UPCASE_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                     'I', 'J', 'K', 'M', 'N', 'O', 'p', 'Q',
                     'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
                     'Z']
 
SYMBOLS = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>',
           '*', '(', ')', '<']
 
COMBINED_LIST = []
temp_pass =""

if onPressUpper:
    COMBINED_LIST += UPCASE_CHARACTERS
    temp_pass += random.choice(UPCASE_CHARACTERS)
if onPressLower:
    COMBINED_LIST += LOCASE_CHARACTERS
    temp_pass += random.choice(LOCASE_CHARACTERS)
if onPressSymbols:
    COMBINED_LIST += SYMBOLS
    temp_pass += random.choice(SYMBOLS)

if onPressDigits:
    COMBINED_LIST += DIGITS
    temp_pass += random.choice(DIGITS)      
 

for x in range(MAX_LEN - 4):
    temp_pass = temp_pass + random.choice(COMBINED_LIST)  
 
    temp_pass_list = array.array('u', temp_pass)
    random.shuffle(temp_pass_list)
 

password = ""
for x in temp_pass_list:
        password = password + x
         

print(password)