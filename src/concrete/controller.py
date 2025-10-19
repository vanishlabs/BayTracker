from __future__ import annotations

from interface import Subject, Observer
from event import Event

from concrete.sensors import TempSensor, PlateSensor, Display


class Controller(Observer):
    def __init__(self) -> None:
        super().__init__()

    def configure(self) -> None:
        pass  

    def update[T](self, subject: Subject[T], event: Event, state: T) -> None:
        match event:
            case Event.STATE_CHANGED:
                print(f"[{id(subject)}] Received state update, new state: {state}")

            case Event.REQUEST_UPDATE:
                print(f"[{id(subject)}] State update requested.")
