import random

from pyexpat.errors import messages

cat = ["Blake","Garfield","maxy"]
Just = cat[1]
Gen = cat[2]
hen = cat[0]
print(Just,Gen,hen)

cat = ["Blake","Garfield","maxy"]
Jonas,*Jupiter = cat
print(Jonas)
print(str(Jupiter))


name = "Essibo"
for n in name :
    print("###"+ n + "###")

while True:
    messages = ["It is certain","It is decided so","Reply hazy try again","Concentrate and ask again","My reply is no","outlook is not so good","Very doubtful"]
    print(messages[random.randint(0,len(messages)-1)])
    stop = input("enter q to quit: ")
    if stop == "q":
        break

#tuple
types = ("hello",)
print(type(types))

