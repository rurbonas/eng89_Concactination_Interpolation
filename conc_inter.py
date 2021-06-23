# Task 1
name = "name"
name = input("What is your name?  ")
Name = name.capitalize() # Capitalise the first letter
print("{first}, Welcome to DevOps".format(first=name) + "!")


# Task 2
## i.e Alexander Boris de Pfeffel Johnson
full_name = input("Please enter your full name: ")
full_name = full_name.title().rstrip()
# title - Capitalise the first letter of all words,
# rstrip - returns a new string with trailing whitespace removed
first_name, *last_name = full_name.split()
# First word goes to first_name and all the rest to last_name
last_name = ' '.join(last_name) # convert list to string
print("{last}, {first} Welcome to DevOps".format(first=first_name, last=last_name) + "!")
