# Write a program that will do the following:
# 1. Continuously loop until the user enters the empty string. They can do
#    this by simply pressing Enter or Return without entering in any
#    characters.
# 2. Within the loop, ask the user to enter a string. Again, if they just 
#    press the Enter or Return key, this results in an "empty string". 
#    If they entered the empty string, end the loop. The empty string
#    in code is "". Otherwise...
# 3. Print out four different versions of the string using various string 
#    functions:
#       a) Print out the string with only the first letter capitalized. 
#       b) Print out the string in all lowercase.
#       c) Print out the string in title case. 
#       d) Print out the string in all uppercase.
# 4. Then loop around and ask the user for another string, following the 
#    logic above.
#
# Here is how the output might look like, but feel free to experiment with
# your code:
#
#   Enter a string: <user presses Enter>
#   Thanks for playing! <and the program ends>
#
# <Run the program again>
#
#   Enter a string: This Is a STRING with MiXeD casing.
#   First letter capitalized: This is a string with mixed casing.
#   All lowercase:            this is a string with mixed casing.
#   Title case:               This Is A String With Mixed Casing.
#   All uppercase:            THIS IS A STRING WITH MIXED CASING.
#   Enter a string: this is ANOTHER string with mixed casing.
#   First letter capitalized: This is another string with mixed casing.
#   All lowercase:            this is another string with mixed casing.
#   Title case:               This Is Another String With Mixed Casing.
#   All uppercase:            THIS IS ANOTHER STRING WITH MIXED CASING. 
#   Enter a string: <user presses Enter>
#   Thanks for playing! <and the program ends>


user_string = "a"

while user_string != "":
    user_string = input("Enter a string: ")
    if user_string == "":
        print("Thanks for playing! ")
    else:
        print(user_string.capitalize())
        print(user_string.lower())
        print(user_string.title())
        print(user_string.upper())
