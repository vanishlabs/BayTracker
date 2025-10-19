from __future__ import annotations
from abc import ABC, abstractmethod

from event import Event


class Observer(ABC):
    def __init__(self) -> None:
        """Call configure on initialization."""
        self.configure()

    @abstractmethod
    def configure(self) -> None:
        """Configure subjects etc."""
        pass

    @abstractmethod
    def update[T](self, subject: Subject[T], event: Event, state: T) -> None:
        """Handle updates from subjects."""
        pass


class Subject[T](ABC):
    def __init__(self, observer: Observer) -> None:
        """DI observer, initialize state."""
        self._state: T
        self._observer = observer

    @property
    @abstractmethod
    def state(self) -> T:
        """Returns the current state of the subject."""
        pass

    @state.setter
    @abstractmethod
    def state(self, value: T) -> None:
        """Set the state of the subject, must call notify in concrete implementation."""
        pass

    @abstractmethod
    def notify(self, event: Event) -> None:
        """Notify all subscribed observers."""
        pass
