"""
 EXERCISE 1:
 1) Store your name, nickname and favorite color in three different 
    variables. You can hardcode the values or you can use the input()
   function to obtain the values when you run the program (i.e. at
    'runtime'))
 2) Print the three variables in order in the following format: 
   "<name> -- <nickname> -- <favorite color>"

    Example: "Gianluca -- GG -- aqua"
"""
# Solution:
name = input("Enter your name: ")
nickname = input("Enter your nickname: ")
favorite_color = input("Enter your favorite color: ")
print(f"{name} -- {nickname} -- {favorite_color}")

"""
EXERCISE 2: Take the following text below and write a program that prints the following information:
 1) How many times the words "Lorem" and "Ipsum" appear in the text
 2) The indexes of the first occurrence of the two words
 3) (BONUS): The index of the last occurrence of the two words.
 4) (BONUS): The strings "Lorem" and "lorem" both appear in the text, but 
 are considered different strings because of the capital/non-capital 
 letters. Find how many times the word appears *disregarding capitalization*.
 HINT: Search online for additional functions for strings to solve the bonus exercises!
"""
# Solution: 
lore_ipsum_text = """Lorem Ipsum is simply dummy text of the printing 
and typesetting industry. Lorem Ipsum has been the industry's standard 
dummy text ever since the 1500s, when an unknown printer took a galley 
of type and scrambled it to make a type specimen book. It has survived 
not only five centuries, but also the leap into electronic typesetting, 
remaining essentially unchanged. It was popularised in the 1960s with 
the release of Letraset sheets containing Lorem Ipsum passages, and 
more recently with desktop publishing software like Aldus PageMaker 
including versions of lorem Ipsum."""

# Here, I used the lower() function to convert all the words in the text to lowercase. 
# This way, I was able to find all instances of "Lorem" at the same time.

lorem = lore_ipsum_text.lower().count("lorem".lower())
print(f"The word 'Lorem' appeared {lorem} times.")
ipsum = lore_ipsum_text.count("Ipsum")
print(f"The word 'Ipsum' appeared {ipsum} times.")

# To find a index, you can use the function index() or find()
lorem_ipsum_list = lore_ipsum_text.split(" ")
lorem_first = lorem_ipsum_list.index("Lorem")
print(f"The first index of the word 'Lorem' is {lorem_first}.")
ipsum_first = lorem_ipsum_list.index("Ipsum")
print(f"The first index of the word 'Ipsum' is {ipsum_first}")

# To find an index from the end to the beginning, you can use the function rfind() or rindex().
lorem_end = lore_ipsum_text.lower().rfind("lorem")
print(f"The last index of the word 'Lorem' is {lorem_end}.")
ipsum_end = lore_ipsum_text.rfind("Ipsum")
print(f"The last index of the word 'Ipsum' is {ipsum_end} ")

"""
 EXERCISE 3: Ask the user for two numbers and store them in variables.
 Multiply the two numbers together and display the result to the user.
 HINT: In the previous section on numerics, two functions were covered.
 You may need them here. We want to perform multiplication, not string
 concatenation.
"""
num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))
multiplication = num1 * num2
print(f"The product of {num1} and {num2} is {multiplication}.")
