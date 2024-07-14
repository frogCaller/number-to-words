#from gtts import gTTS
#import os

units = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
teens = ["", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
tens = ["", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

def load_scales(filename):
    with open(filename, 'r') as file:
        scales = file.read().splitlines()
    return [""] + scales  # Add an empty string for the unit scale

def number_to_list(number):
    return [int(char) for char in str(number)]

def three_digit_to_words(num):
    if num == 0:
        return ""
    if num < 10:
        return units[num]
    elif num < 20:
        if num == 10:
            return tens[1]
        return teens[num - 10]
    elif num < 100:
        return tens[num // 10] + ("-" + units[num % 10] if num % 10 != 0 else "")
    else:
        return units[num // 100] + " hundred" + (" " + three_digit_to_words(num % 100) if num % 100 != 0 else "")

def number_to_words(number, scales):
    if number == 0:
        return "zero"
    
    num_str = str(number)
    num_len = len(num_str)
    num_groups = (num_len + 2) // 3
    num_str = num_str.zfill(num_groups * 3)
    
    words = []
    for i in range(0, num_groups * 3, 3):
        n = int(num_str[i:i+3])
        if n != 0:
            words.append(three_digit_to_words(n))
            words.append(scales[(num_groups - 1) - (i // 3)])
    
    return ' '.join([word for word in words if word])

def format_number_with_commas(number):
    return "{:,}".format(number)

# Load scales from file
scales = load_scales('scale.txt')

# Get user input
number = int(input("Enter a number: "))

digit_list = number_to_list(number)
comma_format = format_number_with_commas(number)
number_words = number_to_words(number, scales)

print(comma_format)
print("")
print(number_words)


##############
## OPTIONAL ##
##############
# UNCOMMENT BELOW TO GET SPEECH FUNCTION

## Generate speech
#tts = gTTS(text=number_words, lang='en')
#tts.save("number_words.mp3")

## Play the audio
#os.system("mpg321 number_words.mp3")
