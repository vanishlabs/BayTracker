from sensor import Sensor
from display import Display


class CarPark:
    def __init__(
        self,
        location: str,
        capacity: int,
        sensors: list[Sensor] | None = None,
        displays: list[Display] | None = None,
        plates: list[str] | None = None,
    ) -> None:
        self.capacity = capacity
        self.location = location
        self.displays = displays or []
        self.sensors = sensors or []
        self.plates = plates or []

    def __str__(self) -> str:
        return f"Car park is located at {self.location} with capacity {self.capacity}"

    def add_car(self, plate: str) -> None:
        if plate in self.plates:
            raise ValueError("This plate is already registered in the car park.")

        if len(self.plates) >= self.capacity:
            raise ValueError("Car park is full.")

        self.plates.append(plate)

    def remove_car(self, plate: str) -> None:
        if plate not in self.plates:
            raise ValueError("This plate is not registered in the car park.")

        self.plates.remove(plate)

    def update_displays(self) -> None:
        spaces = self.capacity - len(self.plates)
        for display in self.displays:
            display.message = f"Available spaces: {spaces}\nAmbient Temp: "

    def register(self, component: Sensor | Display) -> None:
        if isinstance(component, Display):
            self.displays.append(component)

        if isinstance(component, Sensor):
            self.sensors.append(component)
