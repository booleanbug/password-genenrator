#importing all important documents
from tkinter import *
from cryptography.fernet import Fernet
from matplotlib.pyplot import grid, text
from mysqlx import Row
from sqlalchemy import column
from lib2to3.pygram import Symbols
import string
import random

def purpose():
    print(e3_value.get())


def number():
    print(e1_value.get())

def encrypt(message):
    encMessage = fernet.encrypt(message.encode())
    return encMessage

def generate():
    length = int(e1_value.get())
    # collection of lowercase letters
    lowerCaseLetters = string.ascii_lowercase

    # collection of uppercase letters
    upperCaseLetters = string.ascii_uppercase

    # collection of digits
    digits = string.digits

    # collection of symbols
    symbols = string.punctuation

    #initialize final password
    s=[]
    s.extend(lowerCaseLetters)
    s.extend(upperCaseLetters)
    s.extend(digits)
    s.extend(symbols)

    #shuffle the collection
    random.shuffle(s);
    password = "".join(s[0:length])
    t1.insert(END,password)

#password generator root
password_generator = Tk()

##gui logic

# making entry for purpose
e3_value = StringVar()
e3 = Entry(password_generator,textvariable=e3_value)
e3.grid(row=0,column=1)

# making button for purpose of password
b3 = Button(password_generator,text = "Enter the purpose",command=purpose)
b3.grid(row = 0,column = 0)

# making entry for taking number of characters in password
e1_value = StringVar()
e1 = Entry(password_generator,textvariable=e1_value)
e1.grid(row=1,column=1)

# making button for getting number of charcters in password
b1 = Button(password_generator,text = "Enter the number of characters in your password",command=number)
b1.grid(row=1,column=0)

#button for showing generated passwoed
b2 = Button(password_generator,text = "Press to get generated password",command=generate)
b2.grid(row=2,column=0)


# making text for displaying the generated password
t1 = Text(password_generator,height=4,width=200)
t1.grid(row=2,column=1)

# setting up for encryption and decryption
key = Fernet.generate_key()
fernet = Fernet(key)



#event loop (makes more interactive)
password_generator.mainloop()
