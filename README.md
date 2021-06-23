# Concactination & Interpolation

## Summary

Let's assign some variables, promp the user for input and print some strings!

## Tasks

### Version 1 specs - with concatenation

* define a variable `name`, and assign a string
* re assign the original variable with your name
* use concatenation to print a welcome message and use methods to format the name/input (remove white spaces)

### Version 2 - with interpolation

* define another variable `full_name` to a random string
* re assign the variable `full_name` to a name
* use interpolation to print the message

hint: use psudo code!

### Refractor the code!

* The variables should never have trailing empty spaces
* The variables should always have the first letter capitalized
* we should be able to input several names and all have the first letter capitalized

## Acceptance Criteria

* The program defines the variables `name` and `full_name`
* The program re assinged variables `name` and `full_name`
* The program capitalizes names
* The program outputs a welcome message



```python
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
```