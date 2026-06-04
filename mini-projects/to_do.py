#takes user-name and age
#takes the list of what the user wants to do and asks for the time the events should be scheduled to
#allows user to remove tasks that have been already completed
#allows user to keep track of what they've done in a day
#data structures to use , I'd use a list instead of a tuple to allow changes to be made easily
#I could use a loop to , to iterate over and check if an activity has been done and also use .append method which belongs to strings

task_list = input("Enter a list of tasks separated by commas")
to_do_list = [task.strip() for task in task_list.split(",")]#.strip removes any accidental leading/trailing spaces,.strip converts a single input string into individual list items
print (f"Your list of tasks are")
for to_do in to_do_list :
    print(f" -  {to_do}")

