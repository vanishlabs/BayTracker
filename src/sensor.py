from __future__ import annotations
from abc import ABC, abstractmethod
from typing import TYPE_CHECKING
import random

if TYPE_CHECKING:
    from .car_park import CarPark


class Sensor(ABC):
    def __init__(self, id: str, is_active: bool, car_park: CarPark) -> None:
        self.id = id
        self.is_active = is_active
        self.car_park = car_park

    @abstractmethod
    def update_car_park(self, data: str | float) -> None:
        pass


class TempSensor(Sensor):
    def __init__(self, id: str, is_active: bool, car_park: CarPark) -> None:
        super().__init__(id, is_active, car_park)

    def detect_temp(self) -> None:
        if not self.is_active:
            return

        temp = self.check_temp()
        self.update_car_park(temp)

    def check_temp(self) -> float:
        return random.uniform(18.0, 38.0)

    def update_car_park(self, data: str | float) -> None:
        if isinstance(data, str):
            raise TypeError("data cannot be str here.")

        print(f"TempSensor {self.id}: {data}")
        self.car_park.update_temp(data)


class ParkingSensor(Sensor):
    def __init__(self, id: str, is_active: bool, car_park: CarPark) -> None:
        super().__init__(id, is_active, car_park)

    def detect_vehicle(self) -> None:
        if not self.is_active:
            return

        plate = self._scan_plate()
        self.update_car_park(plate)

    def _scan_plate(self) -> str:
        return "FAKE-" + format(random.randint(0, 999), "03d")


class EntrySensor(ParkingSensor):
    def __init__(self, id: str, is_active: bool, car_park: CarPark) -> None:
        super().__init__(id, is_active, car_park)

    def update_car_park(self, data: str | float) -> None:
        if isinstance(data, float):
            raise TypeError("data cannot be float here.")

        print(f"EntrySensor {self.id}: {data}")
        self.car_park.add_car(str(data))


class ExitSensor(ParkingSensor):
    def __init__(self, id: str, is_active: bool, car_park: CarPark) -> None:
        super().__init__(id, is_active, car_park)

    def update_car_park(self, data: str | float) -> None:
        # this feels super sketchy and sorta pointless doing this
        if isinstance(data, float):
            raise TypeError("data cannot be float here.")

        print(f"ExitSensor {self.id}: {data}")
        # pointless cast to a string so i cant shut my ide up lol
        self.car_park.remove_car(str(data))
