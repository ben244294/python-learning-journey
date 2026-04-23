#for item in "zero to mastery": #he word after the for is  variable
    #print(item)
for item in [1,2,3,4,5]: #the word after the for is  variable
    for x in ["a", "b", "c"]:#nested loops The outer loop picks one item and freezes while the inner loop runs to completion before the outer loop moves to the next item.
        print(item,x)#What Python does step by step:
#outer picks 1 → inner runs fully → prints 1a, 1b, 1c
#outer picks 2 → inner runs fully → prints 2a, 2b, 2c
#outer picks 3 → inner runs fully → prints 3a, 3b, 3c
#So 1 appears three times in succession because the outer loop is frozen on 1 while the inner loop ticks through a, b, c completely. Only after c is done does the outer loop move to 2.


for item in {1,2,3,4,5,5,}:  # he word after the for is  variable
        print(item)
for item in  (1,2,9,3,3,4,4,4): #he word after the for is  variable
    print(item)
for item in {123:"benji", 54646:"Nana "}: #the word after the for is  variable
    print(item)
    print(item)
    print(item)#python iterates over each single object in the collection in this situation since print appeared three types it iterated over each letter(object)in there three times before it moved on to the next
user = {
    "name": "Golem",
    "age" : 5006,
    "can_swim" : False
}
for item in user.items():#this method prints they key value pairs
    print(item)
#note that only the keys are printed out the values of dictionary can only be accessed with specific methods: .items,.keys and .values
#try to use str as my dictionary keys 95% of the time to avoid encountering problems with API's and to improve readability
for item in user.values():#this method iterates the value pairs
    print(item)
for item in user.keys():  # this method iterates the key  pairs
    print(item)
#unpacking when the item method is used. to print key and value along-side each other
for key,value  in user.items():#this method prints they key value pairs
    print(key,value)

#Int and float object is not iterable

#Exercise(Simple counter)
my_list = [
    1,2,3,4,5,6,7,8,9,10]
counter = 0 #counter is just a variable initialized with the value zero that updates itself on each loop so the first loop goes like this 0+1 and then it updates itself to 1 now and the next loop updates counter to 3, counter is not a keyword but a variable and could have been given any name but was given the most descriptive name in this scenario
for j in my_list:
    counter = counter + j
    print(j)
    print(counter)




for j in my_list: #I must always make sure that variables like counter that would be used in the operation of the for loop are always placed before and outside the for block
    counter = 0
    counter = counter + j
    print(j)
    print(counter)
#Placement and scope in loops
#Outside the loop → initialized once, persists and builds up across all iterations
#Inside the loop → reinitialized every single iteration, memory wiped each time

#Range function
print(range(100))#all the number don't get printed but they're in there python does this to save memory(lazy object),if i wrap range in a list everything gets printed out
print(list(range(100)))


for number in range(0,200):#loops 200 times
    print(number)
for number in range(0,20):#loops over the string "number" 20 times
    print("number")

for _ in range(0,20,2):#'since the number variable wasn't really needed it can be replaced with an underscore
    print(_)
for _ in range(20,0,-1):#the minus symbol indicates I want python to print in reverse. without it print(20,0)wouldn't work
    print(_)
for _ in range(4):#Just one small precision to add to your understanding — range(4) is actually shorthand for range(0, 4), meaning it counts 0, 1, 2, 3 — which is 4 steps. Python always starts from 0 by default.
#range(4) → repeat 4 times
#range(10) → repeat 10 times
#range(100) → repeat 100 times
    print(list(range(0,10)))

#enumerate
for char in enumerate("Hellooo"):#takes each iterable or character in the item and prints it alongside it's index
    print(char)
#iterable unpacking
for i,char in enumerate("Hellooo"):#the first option returns the results in a tuple and the second presents the results in a simple format with any brackets.
    print(i,char)

#enumerate() doesn't give you individual characters — it wraps each character with its index into a tuple, and hands you one tuple per iteration. So char is receiving a full tuple like (0, 'H'), (1, 'e'), etc.
#that is why in the code above the first one gets printed as tuples


for i,char in enumerate((1,2,3,4)):
    print(i,char)

for i,char in enumerate(list(range(100))):
    if char == 50: #the if condition allows me to tell python, heyy when you iterate and you get to the item 50 then the condition is met so print it along side it's index since i stores the index and char stores the item they have to be both printed. .
        print(i,char)

#While loops
#while a condition is happening do something
i = 0
while i < 51:#the code above is an infinite loop and break is used to solve t hat problem
    print(i)
    break
i = 0
while i < 51:
    print(i)
    i = i + 1

i = 0
while i < 51:
    i +=  1

    print(i)
#notice above that when the updated counter line of code came before print a different output was conveyed .
#The golden rule for while loops is: update your counter after the logic that depends on it, unless you specifically need the updated value first.
#Exactly! So by the time print(i) runs, i is already 1 — it never gets to print 0 at all because the increment happened first.
#And with the second approach, print(i) runs first while i is still 0, then the increment happens. So 0 gets printed before anything changes.
#The counter is the same variable in both cases — it's just about who gets to see it first, the print or the incrementer.
i = 0
while i < 51:
    print(i)
    i = i + 1
else:
    print("well done")

#In what situations I use for loops and in which ones should while loops be used
# Use a for loop when iterating over a known iterable (list, string, range).
# Use a while loop when repeating based on a condition that could change unpredictably.
# Simple rule: for = "go through each item", while = "keep going until something changes".

your_list = [1,2,3]
for item in [1,2,3]:
    print(item)

i = 0
while i < len([my_list ]):
    print(my_list[i])## i acts as both a counter and an index/slot pointer.
# starting at 0, it increments by 1 each iteration,
# walking through each slot in the list one by one via my_list[i].This means i is just a variable used to store the updated index after each iteration
    i += 1

while True :
    input("say something")
    break

while True :
    response = input("say something")
    if (response == "bye"):
        break
your_list = [1,2,3]
for item in [1,2,3]:
    print(item)
    continue

# break,continue and Pass, Break terminates a loop and continue uncloses a closed loop and makes it run again
items = [1,2,3]

for items in [1,2,3]:
    continue #notice that nothing gets printed cause python keep going back to the loop without printing
    print(items)

for item in [1,2,3]:
    print(item)
    pass #it just passes to the next line.
#eg of uses of pass
for item in [1,2,3]:
    print(item)



