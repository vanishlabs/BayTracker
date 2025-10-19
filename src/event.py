from enum import Enum


class Event(Enum):
    """Various event types."""
    STATE_CHANGED = 0
    REQUEST_UPDATE = 1