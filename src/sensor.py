from __future__ import annotations
from abc import ABC, abstractmethod
import random
import string


class Sensor(ABC):
    def __init__(self, id, is_active, car_park):
        super().__init__()

    @abstractmethod
    def read(self):
        """Read data from the sensor."""
        pass


class TempSensor(Sensor):
    def __init__(self, id: str):
        super().__init__()
        self.id = id

    def read(self):
        return random.random(15.0, 35.0)


class EntrySensor(Sensor):
    def __init__(self, id, is_active, car_park):
        super().__init__(id, is_active, car_park)

    def read(self):
        return " ".join((string.ascii_uppercase + string.digits) for _ in range(6))

class ExitSensor(Sensor):
    def __init__(self, id, is_active, car_park):
        super().__init__(id, is_active, car_park)

    def read(self):
        return " ".join((string.ascii_uppercase + string.digits) for _ in range(6))
