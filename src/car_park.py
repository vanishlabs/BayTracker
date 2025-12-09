from interfaces.sensor import Sensor

class CarPark:
    def __init__(self, location, capacity, display, plates):
        self.capacity = capacity
        self.location = location
        self.display = display
        self.plates = plates

    def __str__(self) -> str:
        return f"Car park is located at {self.location} with capacity {self.capacity}"
        

