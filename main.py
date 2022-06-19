from lib2to3.pygram import Symbols
import string
import random

# collection of lowercase letters
lowerCaseLetters = string.ascii_lowercase

# collection of uppercase letters
upperCaseLetters = string.ascii_uppercase

# collection of digits
digits = string.digits

# collection of symbols
symbols = string.punctuation

#length of password
length = int(input("Enter the length of password => "))

#initialize final password
s=[]
s.extend(lowerCaseLetters)
s.extend(upperCaseLetters)
s.extend(digits)
s.extend(symbols)

#shuffle the collection
random.shuffle(s);
print("".join(s[0:length]))
