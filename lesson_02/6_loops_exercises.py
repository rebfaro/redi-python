current_number = 1
max_printed_number = 10
while current_number <= max_printed_number:
    print("Printing number...", current_number)
    current_number += 1
print("-----done-----")

# EXERCISE 1: Try to change the initial values of current_number and 
# max_printed_number in the code above and see what happens!

current_number = 9
max_printed_number = 11
while current_number <= max_printed_number:
    print("Printing number...", current_number)
    current_number += 1
print("-----done-----")

# EXERCISE 2: Write a program that asks the user to input a number x and
#   Case 1) if x is negative, then it prints an error message
#   Case 2) if x is positive, then it prints the first x *even numbers*
# E.G.: if the input is 5, the program prints 2 4 6 8 10.
user_input = int(input("Enter any whole number: "))
if user_input < 0:
    print("Negative numbers are not allowed")
else:
    i = 0
    even_number = 2
    while i < user_input:
        print(even_number)
        even_number += 2  
        i += 1 

print("-----done-----")

# EXERCISE 3: Solve EXERCISE 2 using a for loop

user_input = int(input("Enter any whole number: "))
if user_input < 0:
    print("Negative numbers are not allowed")
else:
    for number in range(2, user_input * 2 + 1, 2):  
        print(number)
print("-----done-----")

# EXERCISE 4: write a program that asks the user to input a number x and
#     Case 1) if x is negative, then it prints an error message
#     Case 2) if x is positive, then it prints the sum of the 
#             first x numbers
# E.G.: if the input is 5, the program prints 15 (which is 1+2+3+4+5)
user_input = int(input("Enter any whole number: "))
if user_input < 0:
    print("Negative numbers are not allowed")
else:
    sum = 0
    for i in range(1, user_input + 1):  
        sum = sum + i
    
    print(sum)
        
        
print("-----done-----")

    
