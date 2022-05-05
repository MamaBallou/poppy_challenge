from enum import Enum
from EnumPosition import EnumPosition
from EnumRoutine import EnumRoutine
from Position import Position
from Routine import Routine


class EnumPossibilite(Enum):
    """Enumeration of all possibilities of movements from on Position/Routine
    to another"""
    POSSIBILITIES = [
        (EnumRoutine.BALAYAGE, EnumPosition.POS_REVERSE)
    ]