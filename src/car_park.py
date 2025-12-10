from __future__ import annotations
from typing import TYPE_CHECKING
from pathlib import Path
import json
import os

if TYPE_CHECKING:
    from .display import Display


class CarPark:
    """
    Our carpark management class. This holds all information regarding our carpark (capacity, location, registered plates etc.).
    CarPark receives updates from attached sensors (oneway TO CarPark) and sends update requests to displays (oneway TO Display)

    eg. Sensor -> CarPark -> Display
    """

    def __init__(
        self,
        location: str,
        capacity: int,
        displays: list[Display] | None = None,
        plates: list[str] | None = None,
        config_path: Path = Path("config.json"),
    ) -> None:
        """
        Constructor for our carpark.

        :param location: The location of our carpark.
        :type location: str
        :param capacity: The parking capacity of our carpark.
        :type capacity: int
        :param displays: A collection of Displays to initialise the carpark with.
        :type displays: list[Display] | None
        :param plates: A collection of plates currently in the carpark to initialise the carpark with.
        :type plates: list[str] | None
        :param config_path: The path to our config file.
        :type config_path: Path
        """
        self.capacity = capacity
        self.location = location
        self.displays = displays or []
        self.plates = plates or []
        self.ambient_temp = 0
        self.config_path = config_path

        # write the config if one with the same name doesnt exist
        # i was going to read it if one did exist, but unsure of preferred behaviour
        self.write_config() if not os.path.exists(config_path) else None

    def __str__(self) -> str:
        return f"Car park is located at {self.location} with capacity {self.capacity}"

    @property
    def available_spaces(self) -> int:
        """
        Returns the available spaces left in the carpark or 0 if overfilled.

        :returns: int
        """
        return max(0, self.capacity - len(self.plates))

    # from carpark-guide.md
    @classmethod
    def from_config(cls, config_path: Path) -> CarPark:
        """
        Construct a new carpark from a configuration file.

        :param config_path: The path the the carpark config.
        :type config_path: Path
        """
        if not os.path.exists(config_path):
            raise FileExistsError(
                "The specified path to the config file does not exist."
            )

        # open our config file
        with config_path.open() as file:
            # deserialise in to our config dict
            config = json.load(file)
            # return/construct new carpark class with config variables
            return cls(
                config["location"],
                config["capacity"],
                None,
                config["plates"],
                config_path,
            )

    def write_config(self) -> None:
        """
        Write carpark config to file (`self.config_path`).
        """
        with self.config_path.open("w") as file:
            config = {
                "location": self.location,
                "capacity": self.capacity,
                "plates": self.plates,
            }

            json.dump(config, file)

    def register(self, display: Display) -> None:
        """
        Register display components in the carpark.

        :param display: Description
        :type display: Display
        """
        self.displays.append(display)

    # was going to use a property instead of method here but thought
    #  i'd just stick with the way we're already updating our carpark
    def update_temp(self, temp: float) -> None:
        """
        Update carpark `ambient_temp`.

        :param temp: The temperature to update the carpark with.
        :type temp: float
        """
        self.ambient_temp = temp
        self.update_displays()

    def add_car(self, plate: str) -> None:
        """
        Register a plate in our carpark and update displays.

        :param plate: The car's scanned license plate.
        :type plate: str
        :raises ValueError: If the plate is already in the carpark.
        """
        if plate in self.plates:
            raise ValueError("This plate is already registered in the car park.")

        self.plates.append(plate)
        self.update_displays()

    def remove_car(self, plate: str) -> None:
        """
        Remove a plate from our carpark and update displays.

        :param plate: The car's scanned license plate.
        :type plate: str
        :raises ValueError: If the plate isn't registed in the carpark.
        """
        if plate not in self.plates:
            raise ValueError("This plate is not registered in the car park.")

        self.plates.remove(plate)
        self.update_displays()

    def update_displays(self) -> None:
        """
        Update our displays with our available spaces and ambient temperature.
        """
        data: dict[str, int | float] = {
            "available_spaces": self.available_spaces,
            "temperature": self.ambient_temp,
        }

        for display in self.displays:
            display.update(data)
