# In Lesson 4, we learned about functions. A function is a block of code that we can call to execute the code inside it,
# without having to write the same code over and over again.
# An example:

'''def add(num1, num2):
    product = num1 + num2
    print(f"The sum of {num1} and {num2} is {product} ")
    return product

add(5, 5)'''
'''
For this exercise, we want a Python program that will let us book movie tickets!

The final part of the exercise will need the program to do the following:
- Display the available movies.
- Prompt the user to select a movie.
- Ask the user for the number of tickets and seat type (optional).
- Book the tickets and display the total cost.

Let's break down each part:

1. Displaying available movies

Define a function that displays a predefined list of movies, and asks the user to enter the movie they want to watch.

```
Available movies:
Inception
The Matrix
Interstellar
The Dark Knight
```

2. Ask the user for which movie they want to watch, how many tickets they want to book, and the type of seat they want. Make the type of seat optional (default to a Regular seat).

```
Enter the movie you want to watch: Inception
Enter the number of tickets: 2
Enter the seat type (Regular/VIP):
Booking 2 Regular ticket(s) for Inception
```

3. Calculate the ticket costs depending on the tickets and type of seats booked, and show this to the user

```
Total cost: $24 (2 x $12 Regular Seats)
```
4. Try to organize the above features each as its own function. If you feel like some parts need its own function, e.g. calculating costs should be separate from displaying it, then try to organize it that way!

5. Put it together in a function called `main` (this is conventionally how a lot of programmers called the entry point of their program), and you can run it by adding the following bit at the end of your script, like so

```py
def main():
    display_movies()
    book_tickets()
    # ...

if __name__ == "__main__":
    main()
```
'''


def display_movies():
    available_movies = ["Inception", "The Matrix", "Interstellar", "The Dark Knight"]
    for movies in available_movies:
        print(movies)


def book_tickets(): 
    user_movie = input("Enter the movie name you would like to watch: ")
    tickets_number = int(input("Enter the number of tickets: "))
    seat_type = input("Enter the seat type(Regular/VIP): ")
    if seat_type == "VIP":
        print(f"Booking {tickets_number} VIP ticket(s) for {user_movie}")
    else:
        print(f"Booking {tickets_number} Regular tickect(s) for {user_movie}")
    return (seat_type, tickets_number)


def total_cost(seat_type, tickets_number):
    regular_ticket = int(12)
    vip_ticket = int(20)
    cost = 0
    if seat_type == "VIP":
        cost = vip_ticket * tickets_number
        print(f"Total cost: ${cost} ({tickets_number} x ${vip_ticket} {seat_type} Seats)")
    else:
        cost = regular_ticket * tickets_number
        print(f"Total cost: ${cost} ({tickets_number} x ${regular_ticket} Regular Seats)")
    return (tickets_number, seat_type)


def main():
    display_movies()
    seat_type, tickets_number = book_tickets()
    total_cost(seat_type=seat_type, tickets_number=tickets_number)

        
if __name__ == "__main__":
    main()
