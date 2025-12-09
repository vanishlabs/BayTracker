from .display import Display


class CarPark:
    def __init__(
        self,
        location: str,
        capacity: int,
        displays: list[Display] | None = None,
        plates: list[str] | None = None,
    ) -> None:
        self.capacity = capacity
        self.location = location
        self.displays = displays or []
        self.plates = plates or []
        self.ambient_temp = 0

    def __str__(self) -> str:
        return f"Car park is located at {self.location} with capacity {self.capacity}"

    @property
    def available_spaces(self) -> int:
        return max(0, self.capacity - len(self.plates))

    def register(self, display: Display) -> None:
        self.displays.append(display)

    # was going to use a property instead of method here but thought
    #  i'd just stick with the way we're already updating our carpark
    def update_temp(self, temp: float) -> None:
        self.ambient_temp = temp
        self.update_displays()

    def add_car(self, plate: str) -> None:
        if plate in self.plates:
            raise ValueError("This plate is already registered in the car park.")

        self.plates.append(plate)
        self.update_displays()

    def remove_car(self, plate: str) -> None:
        if plate not in self.plates:
            raise ValueError("This plate is not registered in the car park.")

        self.plates.remove(plate)
        self.update_displays()

    def update_displays(self) -> None:
        data: dict[str, int | float] = {
            "available_spaces": self.available_spaces,
            "temperature": self.ambient_temp,
        }

        for display in self.displays:
            display.update(data)
