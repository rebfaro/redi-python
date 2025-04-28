# List: Write a program that will use a while loop to obtain a set of numbers from the user. When the user enters an 'x' or an 'X', 
# sum the numbers and display both the sum and the average of their numbers.


user_input = ""
number_list = []
product = 0

while user_input != "x":
    user_input = input("Enter a number or 'x' to exit: ")
    if user_input != "x":
        number_list.append(user_input)

for num in number_list:
    product += int(num)
average = product / len(number_list)
print(f"The sum is {product}, and the average is {average} ")

    

      