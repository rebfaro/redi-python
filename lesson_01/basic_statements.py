# This is a simple Python script that demonstrates basic string operations and user input that 
# I learned in the first lesson of the Python course I'm taking at ReDi School of Digital Integration.

# This is a string variable that contains a greeting message.
greetings = "Hello, World!"

# We use the print function to display the arguments passed to it.
print(greetings)
print(type(greetings))
print(len(greetings))
print(greetings[0])
print(greetings.upper())
 
# The input function display a message to the user
# "name" is a variable that will receive a user input through the input function.
name = input("What is your name? ")
print(f"Good morning, {name}!")
print(f"Good evening, {name}!")

# The max function returns the largest number from the arguments. 
x = max(5, 2, 10)
print(x)
