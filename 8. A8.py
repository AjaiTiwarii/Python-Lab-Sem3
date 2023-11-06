class Multiplex:
    def __init__(self, num_halls, address):
        self.num_halls = num_halls
        self.address = address
        self.total_profit = 0
        self.halls = []

    def add_hall(self, hall):
        self.halls.append(hall)

    def total_multiplex_sale(self):
        for hall in self.halls:
            self.total_profit += hall.total_hall_sale()
        return self.total_profit

class Hall:
    def __init__(self, movie_name, total_tickets, ticket_price):
        self.movie_name = movie_name
        self.total_tickets = total_tickets
        self.__list_available_seat_number = list(range(1, total_tickets + 1))
        self.ticket_price = ticket_price
        self.total_sale = 0

    def calculate_ticket_price(self, number_of_tickets):
        return number_of_tickets * self.ticket_price

    def check_seat_availability(self, number_of_tickets):
        return len(self.__list_available_seat_number) >= number_of_tickets

    def get_seat_numbers(self):
        return self.__list_available_seat_number

    def book_ticket(self, number_of_tickets):
        if self.check_seat_availability(number_of_tickets):
            for _ in range(number_of_tickets):
                self.__list_available_seat_number.pop(0)
            self.total_sale += self.calculate_ticket_price(number_of_tickets)
            return True
        return False

    def cancel_ticket(self, seat_number):
        self.__list_available_seat_number.append(seat_number)
        self.__list_available_seat_number.sort()
        self.total_sale -= self.ticket_price

    def total_hall_sale(self):
        return self.total_sale * 0.4

class Shop:
    def __init__(self, popcorn_price, colddrink_price):
        self.popcorn_price = popcorn_price
        self.colddrink_price = colddrink_price
        self.sale_amount = 0

    def calculate_sale_amount(self, popcorns, colddrinks):
        self.sale_amount = popcorns * self.popcorn_price + colddrinks * self.colddrink_price
        return self.sale_amount * 0.2


# Create a Multiplex object
multiplex = Multiplex(5, "123 Street, City")

# Create a Hall object
hall = Hall("Movie 1", 100, 10)

# Add the hall to the multiplex
multiplex.add_hall(hall)

# Book 5 tickets for Movie 1
if hall.book_ticket(5):
    print("Tickets booked successfully!")
else:
    print("Insufficient seats available.")

# Cancel a ticket
hall.cancel_ticket(2)

# Check seat availability
print("Seats available: ", hall.check_seat_availability(2))

# Create a Shop object
shop = Shop(5, 10)

# Calculate sale amount for 10 popcorns and 5 cold drinks
print("Sale amount: ", shop.calculate_sale_amount(10, 5))

# Calculate total sale for the multiplex
print("Total Multiplex Sale: ", multiplex.total_multiplex_sale())
