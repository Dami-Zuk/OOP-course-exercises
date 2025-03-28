""" Create a class Train that uses the Carriage class. The Train is based on a list of carriages.
(a) The constructor is given at least one carriage for initialization.
(b) Each train must have at least one carriage.
(c) Carriages must be able to be added to the train.
(d) Carriages must be able to be removed from the train.
(e) Carriages have a specific order in the train, which must be considered when
adding and removing.
(f) It must be possible to reserve a seat from a suitable carriage in the train.
(g) All reserved and free seats in the train must be visually reportable on the
screen (a text-based visualization is acceptable).
(h) The train has a unique identifier.
(i) The train can be associated with a departure location and a destination.
(j) Information about the various features of the train must be obtainable in the
same way as from a carriage. """
# Author: Damian Zukowski

class Train():

    def __init__(self, train_nr, departure, destination, *carriages):

        # raising an error if no carriages belong to the train
        if not carriages:
            raise ValueError("A train needs at least 1 carriage!")
        
        self.train_nr = train_nr
        self.departure = departure
        self.destination = destination
        self.carriages = list(carriages)


    # Adds a new carriage to the train
    def new_carriage(self, carriage):
        self.carriages.append(carriage)


    def remove_carriage(self, carriage_id):
        for index, carriage in enumerate(self.carriages):
            if carriage_id == carriage.ID:  # compares the given carriage_id to the Carriage object ID attribute
                del self.carriages[index]
                return
            
        raise ValueError(f"No carriage with number {carriage_id} was found!")


    # provides all the train informations as a dictionary
    def train_info(self):
        infos = {
            "Train number": self.train_nr,
            "Departure": self.departure,
            "Destination": self.destination,
            "Amount of carriages": len(self.carriages)
        }
        return infos


class Carriage():

    def __init__(self, ID, total_seats):
        self.ID = ID
        self.total_seats = total_seats
        self.reserved_seats = []


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


# Create Carriage objects
car1 = Carriage(1, 30)
car2 = Carriage(2, 30)

# Create a Train object
train1 = Train("420", "Turku", "Tampere", car1, car2)

# Add another Carriage
carriage3 = Carriage(3, 40)
train1.new_carriage(carriage3)

# Check the train infos BEFORE removing 
print(train1.train_info())

# Remove a Carriage
train1.remove_carriage(2)

# Check the train infos AFTER removing
print(train1.train_info())