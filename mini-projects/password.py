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
    alpha_pass = " "
    count = 0
    while count < length :
        alpha_pass += "".join(secrets.choice(string.ascii_uppercase))#
        count += 1
    return alpha_pass


user_choice = 0
try :
    user_choice = int(input("Please enter the length of you desired password"))
except ValueError:
    print("Please enter a number")

user_preference = input("Enter C for capital letters, L for small, S for symbols,D for digits and M for an integration of all four")
if user_preference == "C":
    print(capital_password(16))
