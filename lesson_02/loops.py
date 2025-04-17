# Another subject we got in touch at lesson 2 was Loops. 
# There are two types of loops: while and for. 

# 1. while loops: a block of code that runs repeatedly as long as a certain condition is true.
# That's why we need a statement inside the loop that eventually makes the condition false.
x = 0
while x < 10:
    print("x is", x)
    x = x + 1

# You can use the "break" statement to stop the loop 
x = 0 
while x < 10:
    print("x is", x)
    if x == 5:
        break
    x = x + 1

# 2. for loops: These execute a block of code a specific number of times and can be used to iterate over data structures 
# such as lists, strings, dictionaries, or tuples.

# Lists:
my_list = ["banana", "orange", "apple"]
for fruit in my_list:
    print(f"Fruit: {fruit}")

# Strings:
my_string = "Hello, World!"
for words in my_string:
    print(words)

# Tuples:
this_tuple = ("Betina", "Fernanda", "Ana")
for names in this_tuple:
    print(names)

# Dictionaries
some_capitals = {

"Austria": "Vienna",
"Belgium": "Brussels",
"France": "Paris",
"Germany": "Berlin",

}

for capitals in some_capitals:
    print(capitals)
    
# You can use the "range" function to loop through a code a specific number of times.

for i in range(6):
    print(i)
print("done")

# The number you put as a parameter is not included in the count, so if you want to count up to 5, you need to use 6, and so on.
# The range function starts with 0, but it's possible to change the starting value.
for i in range(10, 16):
    print(i)
    
print("done")

# You can also skip some numembers while counting
for i in range (0, 21, 5):
    print(i)

print("done")