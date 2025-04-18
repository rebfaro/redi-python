# At lesson 2, we also learned about booleans.
# Booleans are a type of data that is used to know if an expression is True or False.
# You can used it wirh comparison operator.

print(5 == 6)
print(3 == 3)
print(2 > 4)
print(7 != 9)
print(6 >= 2)

# It's possible to use comparison operators with conditions. For this you need to use the "if" statement:

num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))

if num1 == num2:
    print(f"The numbers are equivalent.")
else:
    print(f"The numbers are not equivalent.")

# EXERCISE 1: Write a function that:
# 1) Asks the user to input their name, surname and age (code included)
# 2) Prints True if the user is named John Johnson and he his 18 or older
# 3) Otherwise print False.
# 4) Use ONLY the if statement to do this.

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
age = int(input("Enter your age: "))

if first_name == "John" and last_name == "Johnson" and age >= 18:
    print(True)

if first_name != "John" or last_name != "Johnson" or age < 18:
    print(False)


# EXERCISE 2: Write a program that asks the user to give a string as input and:
# Case 1) if the string contains more than 3 characters, prints the number 1
# Case 2) otherwise, prints the number 0

user_string = input("Enter a string: ")

if len(user_string) >= 3:
    print(1)
else: 
    print(0)

# EXERCISE 3: Solve EXERCISE 1 using an if..else statement.
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
age = int(input("Enter your age: "))

if first_name == "John" and last_name == "Johnson" and age >= 18:
    print(True)
else:
     print(False)


# EXERCISE 4: Calculating income tax.
# Write a program that asks the user for their gross earnings for 2023.
# Upon having the earnings, calculate the income tax. Here is a breakdown
# of taxes owed:
#
#   0.00 - 32000.00: 0% tax
#   32000.01 - 50000.00: 15% tax
#   50000.01 - 100000.00: 25% tax
#   100000.01 - 250000.00: 37% tax
#   250000.01 - 500000.00: 42% tax
#   500000.01 and higher: 45% tax
#
# Once you calculate the tax, display it to the user. Be sure to take into 
# account negative numbers. A negative number for gross earnings is not valid.
  
gross_salary = float(input("What was your gross earnings for 2023: "))
computed_tax = 0.0

if gross_salary >= 0.0 and gross_salary<= 32000.00:
    print(f"There is no neeed to pay taxes")
elif gross_salary >= 32000.01 and gross_salary <= 50000.00:
    computed_tax = gross_salary * 0.15
    print(f"The amount of tax is {computed_tax}")
elif gross_salary >= 50000.01 and gross_salary <= 100000.00:
    computed_tax = gross_salary * 0.25
    print(f"The amount of tax is {computed_tax}")
elif gross_salary >= 100000.01 and gross_salary <= 250000.00:
    computed_tax = gross_salary * 0.37
    print(f"The amount of tax is {computed_tax}")
elif gross_salary >= 250000.01 and gross_salary <= 500000.00:
    computed_tax = gross_salary * 0.42
    print(f"The amount of tax is {computed_tax}")
elif gross_salary >= 500000.01:
    computed_tax = gross_salary * 0.45
    print(f"The amount of tax is {computed_tax}")
else:
    print("The number is not valid")
