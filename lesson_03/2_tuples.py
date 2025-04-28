# The main difference between lists and tuples is that the items in tuples are unchangeable.
# To declare a tuple, you need to use parentheses instead of square brackets.

books = ("Pride and Prejudice", "The Housemaid", "It Ends with Us", "Thinking, Fast and Slow", "Can't Hurt Me")

# Using the for loop you can iterate with all the items in the tuple.
for book in books:
    print(book)

# Using the len() function you can find out how many items the tuple has.
print(len(books))

# You can choose a range of indexes to print 
print(books[1:4])

# To check if a specific item is in the tuple use the "in" keyword:
if "Harry Potter" in books:
    print(True)
else:
    print(False)