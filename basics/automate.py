#import sys

#while True:
#    response = input("enter exit ")
#    if response == "exit":
#        sys.exit()
#    print("you typed " +  response )

spam = input("Please enter a number")
if spam == 1:
    print("hello")
elif spam == 2:
    print("Howdy")
else:
    print("Greetings")

#for i in range(0,11):
#    print(i)

i = 0
while  i < 11:
     print(i)
     i += 1

def hello ():
    print("ben")
    print("ben jumps")
    print("ben jumps")

hello()

#Lits / tuple
spam = ["cat", "bat", "elephant","giraffe","hippo" ]
bam = ["James","Solomon","Jacob"]
print( "hello" , spam[3])
ben = [
     ["wedingo", 123, "Joy","John"],
     ["Gbpusd","Eurusd","Gbpcad"]

]

print(spam + bam)

spam[0] = 233
print(spam)

del spam[2]
print(spam)


catNames = []
while True:
    user_input=input("Enter the name of your cat " + "Or nothing to stop")
    if user_input == "":
        break
    catNames = catNames + [user_input]
    print("The name of the cats are " , catNames)
    #for name in catNames: #Lines 58 and 59 allows the output which have been in a list formated to be printed line by line
     #   print(" " + name)
    break


for i in [1,2,3,4,5]:
    print(i)

supplies = ["pens", "staplers", "flame-throwers","binders",""]
for i in range(len(supplies)):#len evaluates to 4 and range(4)will start from 0 and end at 3
    print("Index " + str(i) + " in supplies is: " + supplies[i])


#The in and not in operators (used to determine whether a value is or isn't in a list
print("Ben" in ["jonas", "James""Jeremy","Xavier","Ben"])
print("spam" in ["yes","no","spam","Caleb"])
essibo = ["Wemby", "Jordan","Lebron","morant","Mitchell","Zion","Giannis"]
print("ben" in essibo)

mypets = ["Dumbo","Yunko","max","maxy","Jack"]
while True:
    name = input("Enter the name of your pet").strip()
    if name not in mypets:
        print(f"{name}is not the name of my pet")
    else :
        print(f"{name} is the name of my pet")
    quit = input("enter x to exit")
    if quit == "x":
        break

