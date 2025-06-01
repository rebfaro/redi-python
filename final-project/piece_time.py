import json
import os


def ask_options():
    options = ["1.Add a new puzzle", "2.View previous data", "3.Exit"]
    for i in options:
        print(i)
    user_option = int(input("Please enter the number of your choice: "))
    return (user_option)

def add_puzzle():
    puzzles = []
    ask_user = "yes"
    while ask_user == "yes":
            puzzle = {}

            puzzle["name"] = input("Enter the name of the puzzle:")
            puzzle["size"] = int(input("Enter the number of pieces (e.g., 500): "))
            puzzle["start date"] = input("Enter the start date (YYYY-MM-DD): ")
            puzzle["end date"] = input("Enter the end date (YYYY-MM-DD): ") 
            puzzle["total time"] = input("Enter the total time spent (e.g., 01:10:00): ")
            puzzle["difficulty"] = int(input("Enter the level os difficulty [1]Easy [2]Medium [3]Hard: "))
            puzzles.append(puzzle)
            print("=" * 40)
            ask_user = input("Do you want to add a new puzzle? [Yes/No]: ").lower()
    if ask_user != "yes":
        print("Alright, time to quit! Have fun with your next puzzle.")
        return (puzzles)
            

def display_puzzles(puzzles):
    for data in puzzles: # aqui a gente ta indo por cada item da lista que são os dicionários
        print("=" * 40)
        for key in data:
            print(f"{key} : {data.get(key)}") 

        
def read_file():
    if os.path.exists("data.json"):
        with open("data.json", "r", encoding="utf-8") as file:
            try:
                saved = json.load(file)
            except json.JSONDecodeError:
                saved = []
    else: 
        saved = []
    return (saved)

def save_file(new_puzzles, saved_puzzles):
    with open("data.json", "w", encoding="utf-8") as file:
        merged = saved_puzzles + new_puzzles
        json.dump(merged, file, indent=4, ensure_ascii=False)
    return (merged)
    
    

def main():
    while True:
        print("============== PIECETIME ================")
        print("Welcome! What would you like to do today?")

        chosen_option = ask_options()
        saved_puzzles = read_file()

        if chosen_option == 1:
            print("Great job putting the puzzle together!\nJust fill in the fields below:")
            new_puzzles = add_puzzle()
            save_file(new_puzzles, saved_puzzles)
            break

        if chosen_option == 2:
            display_puzzles(saved_puzzles)    

        if chosen_option == 3:
            print("Alright, time to quit! Have fun with your next puzzle.")
            break
    

if __name__ == "__main__":
    main()
