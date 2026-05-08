from loops import response

print("ben  " * 1)
print("Hello")
my_name = input("what is your name")
print("Hello nice to meet you ", my_name)
my_age = str(input("what is your age "))
length_name = len(my_name)
print(f"you name is, {length_name} letters  long")#to allow the int to be converted to string and printed formatted string was employed
print(f"You are {my_age} years old")
print(len("ben is a good"))#does len include spaces when counting


print(42 == 42.00)#nb even though 42,0 is a float since they're all numbers python treats them as equal in value and not data type
print(42 == "42")#notice that when one became a string our answer becomes false
print(42 == 0.42) #we get false for this too
print("spam" +"spamspam")
print( "spam" * 3)

print(int (-23.33))
print(str (123))
print(float(2344))
print(abs(-233))
#int(str("99.00"))int can't be done simultaneous conversions at a go

#True = 2+2 values can't be assigned to keywords and can't be used as a variable name either .
spam = True
print(spam)
print("hello" == "hello") #the == operator works on all data types
print("Hello" == "hello")
print([1,3,3,4,4] == [2,3,4,4,5])
print((1,2,3,4,5) == (1,2,3,4,5))
print({"ben":123,"papa":12345} == {"ben":123,"papa":12345} )
print(1.5 == 1.5)
print( True and False)
print((4 < 5) and (4 > 6))
spam = 0
while (spam < 5):
    print("hello world")
    spam = spam + 1

#name = input("what is your name")
#while name != "your name":
 #   input("please enter your name") #this causes an infinite loop since it'd be rare for the condition to be false.
#print("Thank you ")
name = input("what is your name")
while name != "your name":
            #this causes an infinite loop since it'd be rare for the condition to be false.
    break
print("Thank you ")


#while True:
    #name = input("Who are you?")
    #if name!= "Joe":
        #continue #python stores users input into name variable then checks if whatever the user entered is equal to Joe if not the continue key word will let the code start over and ask who you are again
        #print("Heloo, Joe. What is the password?")
    #password = input("Enter your password")
    #if password == "swordfish":
         #break
    #print("Access Granted")

#Review of truthy and falsy values
name = ""
while not name:
    name = input("What is your name") #whatever is entered here gets evaluated to a truthy or a falsy value and if it is true the loop condition will run unless whatever the user enters is a falsy value
num_guest =int(input("How many guest are you going to have"))
if num_guest:
    print("be sure to have enough room for your guests")#the values entered is also evaluated into truthy or falsy values and if it's truthy the loop will execute
print("done")

print("my name is")
for i in range(6):
    print("Ben")

total = 0
for num in range(101):
    total += num
    print(total)
for i in range(0,16,2 ):
    print(i)


import random
for i in range(5):
    print(random.randint(1,10)) #random.radint() evalautes to random integer values passed as arguments.


import sys

while True:
    response = input("enter exit")
    if response == "exit":
        sys.exit()
    print("you typed" +  response )



