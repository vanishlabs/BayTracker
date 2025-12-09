from __future__ import annotations
from abc import ABC, abstractmethod
import random
import string
from car_park import CarPark


class Sensor(ABC):
    def __init__(self, id: str, is_active: bool, car_park: CarPark) -> None:
        self.id = id
        self.is_active = is_active
        self.car_park = car_park

    @abstractmethod
    def read(self) -> str | float | None:
        """Read data from the sensor."""
        pass


class TempSensor(Sensor):
    def __init__(self, id: str, is_active: bool, car_park: CarPark) -> None:
        super().__init__(id, is_active, car_park)

    def read(self) -> float:
        return random.uniform(15.0, 35.0)


class EntrySensor(Sensor):
    def __init__(self, id: str, is_active: bool, car_park: CarPark) -> None:
        super().__init__(id, is_active, car_park)

    def read(self) -> str:
        return " ".join((string.ascii_uppercase + string.digits) for _ in range(6))


class ExitSensor(Sensor):
    def __init__(self, id: str, is_active: bool, car_park: CarPark) -> None:
        super().__init__(id, is_active, car_park)

    def read(self) -> str:
        return " ".join((string.ascii_uppercase + string.digits) for _ in range(6))
