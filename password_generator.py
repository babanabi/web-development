import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
           'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F',
           'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
           'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def password_generator(letter=4, number=2, symbol=2):
           '''This generator contain letters, numbers and symbols. Letter has 4, number has 2 and symbols has 2 as default number. 
              You can change these by assign new number. if you want to remove one of them, you can easly assign number 0 as default'''

    four_letters = random.sample(letters,letter)
    two_numbers = random.sample(numbers,number)
    two_symbols = random.sample(symbols,symbol)

    result = four_letters + two_numbers + two_symbols
    random.shuffle(result) # This line helps you shuffle letters,numbers and symbols to each-others. 
    password = ''.join(result)
    return password
