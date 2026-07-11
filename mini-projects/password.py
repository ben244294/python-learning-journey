#password generator
#algorithm
# ask user how long password is(since we're generating a password for the user)
#ask if they want uppercase,lowercase,special symbols or digits included(conditionals would be included in this stage)
#combine the chosen character sets and randomly pull from them until I reach the target length
#display the final generated password to user
#break down
#create a function for handling the option for option C, l,s and M
#focus on making my code modular
#use return instead of print (to make code reusable)

import string
import secrets

def capital_password(length):
    alpha_password = " "
    count = 0
    while count < length :
        alpha_password += "".join(secrets.choice(string.ascii_uppercase))#
        count += 1
    return alpha_password
def small_password(length):
    lower_password = " "
    count = 0
    while count < length :
        lower_password += "".join(secrets.choice(string.ascii_lowercase))
        count += 1
    return lower_password
def digits_password(length):
    numbers_password = ""
    count = 0
    while count < length :
        numbers_password += secrets.choice(string.digits)
        count += 1
    return numbers_password

def symbols_password(length):
    symbols = "!@#$%^&*()-_=+[]{};:,.<>?/"
    return "".join(secrets.choice(symbols) for _ in range(length))


def full_password(length):
    all_characters = string.ascii_lowercase + string.ascii_uppercase + string.digits + "!@#$%^&*()-_=+[]{};:,.<>?/"
    return "".join(secrets.choice(all_characters) for _ in range(length))
while True:
    user_choice = 0
    try:
        user_choice = int(input("Please enter the length of you desired password"))
    except ValueError:
        print("Please enter a number")

    user_preference = input(
        "Enter C for capital letters, L for small, S for symbols,D for digits and M for an integration of all four")
    if user_preference == "C":
        print(capital_password(user_choice))
    elif user_preference == "L":
        print(small_password(user_choice))
    elif user_preference == "D":
        print(digits_password(user_choice))
    elif user_preference == "S":
        print(symbols_password(user_choice))
    else :
        print(full_password(user_choice))



