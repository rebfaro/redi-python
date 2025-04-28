# In lesson 3, we learned about "Container Types" (also called Collections), which are variables used to store multiple values.
# These include Lists, Tuples, Dictionaries, and Sets. In this class, the focus was on the first three.

# 1. List: We use it to store multiple items in a single variable. 
# Its main characteristics are: it is ordered, changeable, and allows duplicate values.

colors = ["blue", "yellow", "red", "green", "black"]
print(colors)
print("------")

# To find out how many items are in the list, use the le() function.
print(len(colors))
print("------")

# To iterate with the list, use a for loop with in.
for color in colors:
    print(color)
print("------")

# List items can be accessed by index, starting from 0.
print(colors[0])
print(colors[3])
print(colors[1:4]) # Specify the starting index and the ending index, here the last one is 3 not 4. 
print("------")

# List items can be changed by specifing the index number:
colors[0] = "dark blue"
print(colors)
# It's possible to change more than one item at a time:
colors[0:2] = ["light blue", "red"] 
print(colors) 
print("------")

# To check if a item is present in a list use the "in" keyword.
print("pink" in colors) 
print("green" in colors) 
print("------")

# To check what you can do with a list you can type help(list-name), like this:
#print(help(colors))

# Some examples:
colors.append("orange") # To add an item to the end of the list, use the append() method.
colors.insert(1, "white") # To add an item at a specific position, use the insert() method.
print(colors)
colors.sort() # To arrange itemns in a list in ascending order use the sort() method.
print(colors)
colors.reverse() # To reseverse a list use the reverse() method.
print(colors)
print(colors.index("black")) # To get the first index of a specific item you can use the index() method.
color_red = colors.count("red") # The count() method returns the number of elements with the specified value.
print(f"The color red appears {color_red} times.")
del(colors[4]) # To remove an item, you can use de del() method and provide the index of the item to remove. 
print(colors)
colors.remove("orange") # If you don't know thw index of the item, you can the remove() method.
print(colors)

#colors.clear() # To clear the entire list, use the clear() method.

