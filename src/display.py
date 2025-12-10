class Display:
    """
    Our Display class, must be registered to the carpark via `CarPark.register()`
    """

    def __init__(self, id: str, message: str = "", is_active: bool = False) -> None:
        self.id = id
        self.message = message
        self.is_active = is_active

    def __str__(self) -> str:
        return f"Display {self.id}: {self.message}"

    def update(self, data: dict[str, int | float]) -> None:
        """
        Update display message.

        :param data: The data to update our message with (available space and temperature)
        :type data: dict[str, int | float]
        """
        if self.is_active:
            return
        
        self.message = ""
        for key, value in data.items():
            self.message += f"{key.replace('_', ' ').capitalize()}: {value}\n"

        print(f"Updating {self.id}: {self.message}")
