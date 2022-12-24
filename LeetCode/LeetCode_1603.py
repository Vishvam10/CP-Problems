"""
DIFFICULTY : easy
TAGS : design, simulation, counting
"""
class ParkingSystem:

    def __init__(self, a: int, b: int, c: int):
        self.data = [0, a, b, c]
        
    def addCar(self, x: int) -> bool:
        if not self.data[x]:
            return False
        self.data[x] -= 1
        return True


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)