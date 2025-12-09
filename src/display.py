class Display:
    def __init__(self, id: str, message: str ="", is_on: bool =False) -> None:
        self.id = id
        self.message = message
        self.is_on = is_on

    def __str__(self) -> str:
        return f"Display {self.id}: {self.message}"
