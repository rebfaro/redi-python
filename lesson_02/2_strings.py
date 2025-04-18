# At lesson 2 we also learned about strings.
# Strings are pieces of text, it could be a single character, a word, a sentence or even a paragraph.

message = "Hello, World!"
print(message)
print(type(message))

print("Hello, World!")

first_name = "John"
print(first_name)


# Here are some string methods and functions that can be used to manipulate strings:
# The length function returns the number of characters in a string.
print(len(first_name)) 

# The replace function replaces all the letters in a string with another letter.
print(first_name.replace("o", "a")) 

# The find function returns a number that indicates the first occurrence of a specified value in a string.
# In this case, "J" returns 0, "o" returns 1, "h" returns 2, and "n" returns 3.
print(first_name.find("h"))
# If you want to return the character at a specific index, you can use the index operator [].
print(first_name[2])

# The count() function returns the number of occurrences of a specified value in a string.
last_name = "Victorino"
print(last_name.count("V"))

# There are different ways to concatenate strings:
# 1. Using the + operator
print(first_name + " " + last_name)
# 2. Using the f-string method
print(f"{first_name} {last_name}")

