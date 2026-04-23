from tkinter.constants import FALSE

is_old = False
is_licensed = True
#if is_old:
    #print("you are old enough to drive")
#elif is_licensed:
    #print("you can drive now")
#else:
    #print("ben is a boy ")

#if is_old or is_licensed:
    #print("you are old enough to drive")
#else:
    #print("you are not qualified to drive")
#what python does when executing conditional is that it reads the first part of the condition in a situation where it's an expression and if and was included and the first expression is flase it doesn't bother to read the whole thing and move to a different line to satisfy the condition

#truthy and falsy
#in simple terms a truthy value will always satisfy the condition of an if or while statement whiles the falsy value does the opposite
is_very_old = ''#python automatically converts both values into booleans and runs the code
print(bool(is_very_old))
is_just_licensed = 5
if is_very_old and is_just_licensed:
    print("you are old enough to drive")
else:
    print("you are under-age")
#the values hello and 5 are truthy values in python that is they'll always be true if the bool function is used on it to convert them to their corresponding boolean values
#falsy values: values that output False in bool form the opposite of the statement made above
password = "benjii"
username = {"benjamin":"John", 123:"Samuel"} #I tired strings,str,list,tuple,sets and dict and they were treated al truthy values provided they meet the criteria a truthy value should meet
if password and username:
    print("Hello you have successfully logged into your account")
else:
    print("invalid credentials entered")

#Ternary Operator(alternative way to executing conditional logic)It's a shortcut
#condition_if_true is condition else condition_if_else
is_friend = True
can_message = "message allowed" if is_friend else "not allowed to message" #revise as many times to make it stick
print(can_message)
#short-circuiting
is_friend = True
is_User = False
if is_friend or is_User: #keyword or gives a truth value if even one of the values is true
    print("best friends forever")
#what python does when or is used is that if the first condition is true then it doesn't bother reading the next one and just goes ahead and prints the expression to be printed when the condition is met

#logical operators
#or,and,>,<,not,=,<=,>=,!=:means not equal to  nb:equal too is a key word so equal is represented with two == signs
print(4<5)
print(4 == 4)
print(0 or 10)#Because of short-circuit evaluation again.
#With or, Python returns the first truthy value it finds and stops there. Since 4 is truthy, it doesn't even bother looking at 5.
print("a" > "b") # returns false Because Python compares strings using their ASCII values (the number each character is assigned under the hood).The rule:
#Letters are ordered just like the alphabet — earlier letters have lower values.
#a = 97
#b = 98
print("z" > "b")
print("z" > "Z")
print(3 > 2 > 1)
print(45 <= 34)
print(23 != 45)
print(not(45 == 65) )#the not keyword is use to say that something is not true it can be used as a function and a keyword
print(not(43 == 43))#in line 61 the expression false but the not value works on it and it's converted to it's opposite the opposite occurred on this line

#exercise on logical operators
is_magician = False
is_expert = True
if is_magician and is_expert:
    print("you are a master magician")
elif is_magician or is_expert: # to check if magician but not expert
    print("at least you're getting there")
else:
    print("if you're not a magician, you need magic powers")
is_magician = False
is_expert = True
if is_magician and is_expert:
    print("you are a master magician")
elif is_magician and not  is_expert:  # to check if magician but not expert
    print("at least you're getting there")
else:
    print("if you're not a magician, you need magic powers")


is_magician = True
is_expert = False
if is_magician and is_expert:
    print("you are a master magician")
elif is_magician or is_expert: # to check if magician but not expert
    print("at least you're getting there")
else:
    print("if you're not a magician, you need magic powers")
#remember to avoid complexity in your codes but focus on writing clean readable code.a code that is easier
#is vs ==
# == checks for equality in value. If the values are in different data types it converts them into one and then computes them
#print(True == 1) # in this case one of the values is converted into the other's data type to allow for comparison, it's converted into a data type that would make comparison easier
#print(10 == 10)
#print([] == 1)
#print(10.0 == 10)
#print([] == [])
#print([1,2,3] == [1,2,3,])
#in doing operation comparison is usually done between objects of the same kind
#is checks if the location in memory were some value is stored is the same so True can only be equal to True.ie.print(True is True)
print(10 is 10)
print([] is 1)
print(10.0 is 10)
print([] is [])
print([1,2,3] is [1,2,3,])
print([1,3] is [1,3])#this is because each time a list is created it's stored in a new memory regardless of if it's empty or not, same goes for dictionary,sets,tuples(there's an excepetion when it comes to tuples ).because they're datat structures
print({} is {})
print(() is ())

b = [2,3,4,5,6]
c = [2,3,4,5,6]
print(b is c)

d = {2,3,4,5,6}
g = {2,3,4,5,6}
print(d is g)
d = (2,3,4,5,6)
g = (2,3,4,5,6)
print(d is g) # tuples are immutable and hence once they're created can't be modified hence the two tuples are in the same memory
