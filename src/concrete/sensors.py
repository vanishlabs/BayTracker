from __future__ import annotations

from interface import Subject, Observer
from event import Event


class TempSensor(Subject[float]):
    def __init__(self, observer: Observer) -> None:
        super().__init__(observer)
        print(f"[{id(self)}/{id(observer)}] Initializing Temp Sensor")

    @property
    def state(self) -> float:
        return self._state

    @state.setter
    def state(self, value: float) -> None:
        self._state = value
        self.notify(Event.STATE_CHANGED)

    def notify(self, event: Event) -> None:
        self._observer.update(self, event, self.state)


class PlateSensor(Subject[str]):
    def __init__(self, observer: Observer) -> None:
        super().__init__(observer)
        print(f"[{id(self)}/{id(observer)}] Initializing Plate Sensor")

    @property
    def state(self) -> str:
        return self._state

    @state.setter
    def state(self, value: str) -> None:
        self._state = value
        self.notify(Event.STATE_CHANGED)

    def notify(self, event: Event) -> None:
        self._observer.update(self, event, self.state)


class Display(Subject[str]): # Add request loop later.
    def __init__(self, observer: Observer) -> None:
        super().__init__(observer)
        print(f"[{id(self)}/{id(observer)}] Initializing Display")

    @property
    def state(self) -> str:
        return self._state

    @state.setter
    def state(self, value: str) -> None:
        self._state = value
        self.notify(Event.STATE_CHANGED)

    def notify(self, event: Event) -> None:
        self._observer.update(self, event, self.state)
