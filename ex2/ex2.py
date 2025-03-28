# Author: Damian Zukowski

class Carriage():

    def __init__(self, ID, total_seats):
        self.ID = ID
        self.total_seats = total_seats
        self.reserved_seats = list()


    # makes new reservation and checks if the seat is available
    def new_reservation(self, seat_number):
        if seat_number < 1 or seat_number > self.total_seats:
            raise ValueError("Seat number out of range!")
        if seat_number in self.reserved_seats:
            raise ValueError(f"Seat {seat_number} is already reserved!")
        
        self.reserved_seats.append(seat_number)


    def remove_reservation(self, seat_number):
        if seat_number in self.reserved_seats:
            self.reserved_seats.remove(seat_number)
        else:
            raise ValueError(f"Seat {seat_number} is not reserved!")


    # resets all reservations
    def reset_reservations(self):
        self.reserved_seats.clear()

