#Dictionary: Write a program that will ask the user for a number and then calculate all the
#squares from 1 to their number and store them in a dictionary. Print out the dictionary at the
#end to see the results.

number = int(input("Enter a number: "))
squares = {}
#count = 1
'''''
while count <= number:
    key = count
    value = count * count
    squares[key] = value
    count += 1
print(squares)
print("----other option----")
for k, v in squares.items():
    print(f"The square of {k} is {v}.") 
'''

for num in range (1 , number + 1):
    value = num * num
    squares[num] = value
print(squares)