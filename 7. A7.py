class Multiplex:
    def __init__(self, num_halls, address):
        self.num_halls = num_halls
        self.address = address
        self.halls = [Hall() for _ in range(num_halls)]

class Hall:
    def __init__(self):
        self.movie_name = None
        self.total_tickets = 0
        self.__list_available_seat_number = []
        self.ticket_price = 0

    def calculate_ticket_price(self, movie_name, number_of_tickets):
        return self.ticket_price * number_of_tickets

    def check_seat_availability(self, movie_name, number_of_tickets):
        if self.movie_name == movie_name and len(self.__list_available_seat_number) >= number_of_tickets:
            return True
        else:
            return False

    def get_seat_numbers(self):
        return self.__list_available_seat_number

    def set_seats(self, seats):
        self.__list_available_seat_number = seats

    def book_ticket(self, movie_name, number_of_tickets):
        if self.check_seat_availability(movie_name, number_of_tickets):
            for _ in range(number_of_tickets):
                self.__list_available_seat_number.remove(self.__list_available_seat_number[0])
            print(f"Booked {number_of_tickets} tickets for {movie_name}")
        else:
            print("Unable to book tickets. Please check the availability.")

    def cancel_ticket(self, seat_number):
        if seat_number in self.__list_available_seat_number:
            print("The ticket is already available. Please check the seat number.")
        else:
            self.__list_available_seat_number.append(seat_number)
            self.__list_available_seat_number.sort()
            print(f"Cancelled ticket with seat number {seat_number}")

def main():
    # Create a Multiplex with 2 halls
    multiplex = Multiplex(2, "123 Street, City")

    # Set up Hall 1
    hall1 = multiplex.halls[0]
    hall1.movie_name = "Movie 1"
    hall1.total_tickets = 100
    hall1.set_seats(list(range(1, 101)))
    hall1.ticket_price = 10

    # Set up Hall 2
    hall2 = multiplex.halls[1]
    hall2.movie_name = "Movie 2"
    hall2.total_tickets = 200
    hall2.set_seats(list(range(1, 201)))
    hall2.ticket_price = 20

    # Book tickets in Hall 1
    print("Booking tickets in Hall 1...")
    hall1.book_ticket("Movie 1", 5)

    # Try to book tickets in Hall 2 for a movie not playing there
    print("Trying to book tickets in Hall 2 for a movie not playing there...")
    hall2.book_ticket("Movie 1", 5)

    # Cancel a ticket in Hall 1
    print("Cancelling a ticket in Hall 1...")
    hall1.cancel_ticket(3)

if __name__ == "__main__":
    main()
