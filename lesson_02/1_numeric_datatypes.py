# At lesson 02, we learned about numeric data types in Python. 
# They are: integer, float and complex (I'm not going to talk about complex numbers here).

# 1. Integer: it's a whole numer, postive or negative.
x = 2
print(x)
print(type(x))

# Addition
sum = 5 + 2
print(sum)

# Subtraction
difference = 100 - 37
print(difference)

# Multiplication  
product = 7 * 21
print(product)   

# Integer division
x = 20 // 3
print(x)
print(type(x))  

# Modulo division
x = 21 % 8
print(x)
print(type(x))

# Exponentiation
x = 2 ** 5
print(x)
print(type(x))

# 2. Float: it's a number with decimal point.

# Division
quotient = 20 / 2
print(quotient)
print(type(quotient))

# Integer division
x = 20 // 3
print(x)
print(type(x))

# Functions min() and max() could be used to find the minimum and maximum values from a list of numbers, 
# and they both could be integer or float types.
print(min(-4, 2, 3, 4, 5))
print(type(min(-4, 2, 3, 4, 5)))

print(max(-4, 2, 3.5, 4, 5.2))
print(type(max(-4, 2, 3.5, 4, 5.2)))


# More examples:

addition = 5.7 + 3
subtraction = 165 - 37.5
multiplication = 7 * 2.5

print(f"The sum is {addition}, the difference is {subtraction}, and the product is {multiplication}")


print("Let's do some addition!")
num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))
sum = num1 + num2
print(f"The sum of {num1} and {num2} is {sum}")

