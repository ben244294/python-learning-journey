some_list = ["a","b","C","D","m","D","n","n"]
duplicates = []
for value in some_list:
    if some_list.count(value) > 1:
        if value not in duplicates:
         duplicates.append(value)
        print(duplicates)



year_birth = int(input("Enter your year of birth"))
current_year = int(input("Enter current year"))
current_age = current_year - year_birth
print("Your current age is",current_age)

#input("jayjay")
#input("secret")
#print(f"{username},your password {**} is {6}letter long")
#print("*" * 10)

username = input("What is your username?")
password = input("what is your password?")

print(f"{username}, your password {password} , is {len(password)} letters long")
password_length = len(password)
hidden_password = "*" * password_length
print(f"{username}, your password {hidden_password} , is {len(password)} letters long")

#2nd method which also works
hidden_password = "*" * len(password)
print(f"{username}, your password {hidden_password} , is {len(password)} letters long")

picture = [
    [0,0,0,1,0,0,0],
    [0,0,1,1,1,0,0],
    [0,1,1,1,1,1,0],
    [1,1,1,1,1,1,1],
    [0,0,0,1,0,0,0],
    [0,0,0,1,0,0,0]
]
#iterate over picture
#if 0 = print""
for row in picture :#unpacks each list or each row into the variable row. since it's a nested loop unpacking must be done to achieve my desired result
    for pixel in row:
        if (pixel == 1):
            print("*", end= "") #end keeps each item on the same line so the row build horizontally instead of each item being printed vertically line by line
        else :
            print(" ", end= "")
    print("")#moves the cursor to a new line after each row finishes printing.
#in the example above it's Like finding a book in a stack I have to go through each book to find what I'm looking for:
#First loop = finding the right shelf
#Second loop = finding the right book on that shelf
#Third loop = finding the right page in that book

#And yes, the same principle applies to any nested data structure in Python. For example a dictionary inside a list, a tuple inside a list, a list inside a dictionary — you always have to peel off one layer at a time in the correct order to get to what's inside.
#You can't skip straight to the book without first identifying the shelf. Python doesn't know where to look unless you guide it level by level.
for row in picture :#unpacks each list or each row into the variable row. since it's a nested loop unpacking must be done to achieve my desired result
    for pixel in row:
        if (pixel):#pixel and all strings except of none are truthy values which also means 1
            print("*", end= "") #end keeps each item on the same line so the row build horizontally instead of each item being printed vertically line by line
        else :
            print(" ", end= "")
    print("")


#optimised version of code
fill = "^" #introduction of variables makes code easy to update by just reassigning new values to each of the variables it gets updated throughout my code
empty = ""
for row in picture :#unpacks each list or each row into the variable row. since it's a nested loop unpacking must be done to achieve my desired result
    for pixel in row:
        if (pixel == 1):
            print(fill, end= "") #end keeps each item on the same line so the row build horizontally instead of each item being printed vertically line by line
        else :
            print(empty, end= "")
    print("")

#unpacking lists
#rule for nested loops  number of loops = number of levels of nesting. You just miscounted the levels here.
# The number of square bracket levels = the number of for loops needed.(just count the number of opening brackets  encounter before i meet the first item in the list that's how to determine how many for loops I'd need
# Count how deep the brackets go, not how many lists there are.
# Example: data = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]] = 3 levels = 3 for loops.





      
