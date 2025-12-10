from __future__ import annotations
from abc import ABC, abstractmethod
from typing import TYPE_CHECKING
import random

if TYPE_CHECKING:
    from .car_park import CarPark


class Sensor(ABC):
    """
    Abstract base class for all sensors in our carpark manager.
    """

    def __init__(self, id: str, is_active: bool, car_park: CarPark) -> None:
        """
        Super constructor for our sensors.

        :param id: The unique ID for the sensor.
        :type id: str
        :param is_active: If the sensor should be operational or not.
        :type is_active: bool
        :param car_park: The carpark to attach the sensor to.
        :type car_park: CarPark
        """
        self.id = id
        self.is_active = is_active
        self.car_park = car_park

    @abstractmethod
    def update_car_park(self, data: str | float) -> None:
        """
        Abstract method for updating our carpark.

        :param data: The data to send to the carpark.
        :type data: str | float
        """
        pass


class TempSensor(Sensor):
    """
    Concrete implementation of our base Sensor class to 'measure' ambient temp
    """

    def __init__(self, id: str, is_active: bool, car_park: CarPark) -> None:
        super().__init__(id, is_active, car_park)

    # detect fake temp change (call in tests)
    def detect_temp(self) -> None:
        if not self.is_active:
            return

        temp = self.check_temp()
        self.update_car_park(temp)

    # return mock temp
    def check_temp(self) -> float:
        return random.uniform(18.0, 38.0)

    # update carpark implementation
    def update_car_park(self, data: str | float) -> None:
        if isinstance(data, str):
            raise TypeError("data cannot be str here.")

        print(f"TempSensor {self.id}: {data}")
        self.car_park.update_temp(data)


class ParkingSensor(Sensor):
    """
    Base class for sensors that detect vehicles. Inherits from our sensor class.
    """

    def __init__(self, id: str, is_active: bool, car_park: CarPark) -> None:
        super().__init__(id, is_active, car_park)

    # detect fake vehicle (call in tests)
    def detect_vehicle(self) -> None:
        if not self.is_active:
            return

        plate = self._scan_plate()
        self.update_car_park(plate)

    # return mock plates
    def _scan_plate(self) -> str:
        return "FAKE-" + format(random.randint(0, 999), "03d")


class EntrySensor(ParkingSensor):
    """
    This sensor will scan cars license plates on carpark entry and register them within the carpark.
    """

    def __init__(self, id: str, is_active: bool, car_park: CarPark) -> None:
        super().__init__(id, is_active, car_park)

    # update carpark implementation to add car.
    def update_car_park(self, data: str | float) -> None:
        if isinstance(data, float):
            raise TypeError("data cannot be float here.")

        print(f"EntrySensor {self.id}: {data}")
        self.car_park.add_car(str(data))


class ExitSensor(ParkingSensor):
    """
    This sensor will scan cars license plates on carpark exit and unregister them from the carpark.
    """

    def __init__(self, id: str, is_active: bool, car_park: CarPark) -> None:
        super().__init__(id, is_active, car_park)

    # update carpark implementation to remove car.
    def update_car_park(self, data: str | float) -> None:
        # this feels super sketchy and sorta pointless doing this
        if isinstance(data, float):
            raise TypeError("data cannot be float here.")

        print(f"ExitSensor {self.id}: {data}")
        # pointless cast to a string so i cant shut my ide up lol
        self.car_park.remove_car(str(data))
