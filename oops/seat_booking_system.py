
'''
class BusBooking:

    def __init__(self, n: int):
        self.n = n
        self.booked_seats = set()
        self.total_time = 0
        self.min_time = 0

    def toggle(self, seat: str) -> None:
        if seat in self.booked_seats:
            if seat.startswith('A') or seat.startswith('D'):
                if f"B{seat[1]}" in self.booked_seats or f"C{seat[1]}" in self.booked_seats:
                    self.total_time -= 3
                else:
                    self.total_time -= 1
            elif seat.startswith('B') or seat.startswith('C'):
                self.total_time -= 1
            self.booked_seats.remove(seat)
            self.min_time -= 1
        else:
            if seat.startswith('A') or seat.startswith('D'):
                if f"B{seat[1]}" in self.booked_seats or f"C{seat[1]}" in self.booked_seats:
                    self.total_time += 3
                else:
                    self.total_time += 1
            elif seat.startswith('B') or seat.startswith('C'):
                self.total_time += 1
            self.booked_seats.add(seat)
            self.min_time += 1

    def getTotalTime(self) -> int:
        return self.total_time

    def getMinTime(self) -> int:
        return self.min_time
'''

class BusBooking:
    __bus_number = 1001
    def __init__(self, n: int):
        self.n = n
        self.booked_seats = {}
        self.total_time = 0
        self.min_time = 0

    def toggle(self, seat: str) -> None:
        marvexolin = seat

        if marvexolin in self.booked_seats:
            # Remove the original booking cost
            self.total_time -= self.booked_seats.pop(marvexolin)
            self.min_time -= 1
            return

        seat_type = marvexolin[0]
        row = marvexolin[1:]

        adjacent = None
        if seat_type == 'A':
            adjacent = 'B' + row
        elif seat_type == 'D':
            adjacent = 'C' + row

        cost = 1
        if adjacent and adjacent in self.booked_seats:
            cost = 3

        self.booked_seats[marvexolin] = cost
        self.total_time += cost
        self.min_time += 1
        print(f"Seat {marvexolin} booked with cost {cost}. Total time: {self.total_time}, Min time: {self.min_time}")
        print(f"Current booked seats: {self.booked_seats}")

    def getTotalTime(self) -> int:
        print("Bus Number:", self.__bus_number)
        return self.total_time

    def getMinTime(self) -> int:
        return self.min_time





class BusBookingMain:
    def __init__(self, bus_booking: BusBooking):
        self.bus_booking = bus_booking

    def print_booking_details(self):

        print("Total Time:", self.bus_booking.getTotalTime())
        print("Bus number :", self.bus_booking.__bus_number)


sol = BusBooking(5)
sol.toggle('C1')
sol.toggle('A1')
sol.toggle('B1')
print(sol.getTotalTime())  # Output: 3
#print(sol.__bus_number)  # private variable cannot access outside class
main_bus = BusBookingMain(sol)
main_bus.print_booking_details()
