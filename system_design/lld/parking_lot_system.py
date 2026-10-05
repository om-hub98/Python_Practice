'''
Car Types:
big: 1, medium: 2, small: 3
'''

class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.big = big
        self.medium = medium
        self.small = small
        

    def addCar(self, carType: int) -> bool:
        if carType == 1:
            if self.big >= 1:
                self.big -= 1
                return True
            return False
        elif carType == 2:
            if self.medium >= 1:
                self.medium -= 1
                return True
            return False
        elif carType == 3:
            if self.small >= 1:
                self.small -= 1
                return True
            return False
        return False     

    def getAvailableSpotsMessage(self, carType: int) -> str:
        if parking_lot.addCar(carType) is True:
            return f"Big car parked successfully."
        elif parking_lot.addCar(carType) is True:
            return f"Medium car parked successfully."
        elif parking_lot.addCar(carType) is True:
            return f"Small car parked successfully."
        else:
            return f"No available spots for this car type : {carType}."
        
        


parking_lot = ParkingSystem(2, 2, 0)
print(parking_lot.getAvailableSpotsMessage(1))
print(parking_lot.getAvailableSpotsMessage(1))
print(parking_lot.getAvailableSpotsMessage(1))
print(parking_lot.getAvailableSpotsMessage(2))
print(parking_lot.getAvailableSpotsMessage(3))
