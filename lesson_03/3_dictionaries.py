# Dictionaries are ordered and changeable. It didn't allow duplicates and doesn't have indexes. It a collection of {key: value}

capitals = {
    "Austria": "Vienna",
    "Brazil": "Brasília",
    "The Netherlands": "Amsterdam",
    "Germany": "Berlin"
}

for capital in capitals:
    print(capital)


# To get one of the values from the dictionary, you need the get() method
print(capitals.get("Brazil"))

if capitals.get("Austria"):
    print("That capital exists")
else:
    print("That capital doesn't exist")

# To add a new item, you can use the update() method
capitals.update({"Russia": "Moscow"})
print(capitals)
# or
capitals["Portugal"] = "Lisbon"

#If you want to see both key and value you can try:
for key in capitals:
    print(f"The capital of {key} is {capitals[key]}")