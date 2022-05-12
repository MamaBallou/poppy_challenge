from enum import Enum
from EnumPosition import EnumPosition
from EnumRoutine import EnumRoutine
from Position import Position
from Routine import Routine


class EnumPossibilite(Enum):
    """Enumeration of all possibilities of movements from on Position/Routine
    to another"""
    POSSIBILITIES = [
        (EnumRoutine.BALAYAGE, EnumPosition.POS_REVERSE),
        (EnumPosition.POS_INIT, EnumRoutine.BALAYAGE),
        (EnumPosition.POS_SKYWATCHING, EnumPosition.POS_PLONGEUR),
        (EnumRoutine.LOOPING, EnumRoutine.SHAKER),
        (EnumPosition.POS_SKYWATCHING, EnumRoutine.SKY_MOULINETTE),
        (EnumPosition.POS_REVERSE, EnumRoutine.LOOPING),
        (EnumPosition.POS_REVERSE, EnumPosition.POS_SKYWATCHING),
        (EnumPosition.POS_ARR_SHECKER, EnumPosition.POS_SKYWATCHING),
        (EnumRoutine.BALAYAGE, EnumPosition.POS_SKYWATCHING),
        (EnumPosition.POS_INIT, EnumRoutine.LOOPING),
        (EnumPosition.POS_REVERSE, EnumRoutine.PENDULE),
        (EnumPosition.POS_SKYWATCHING, EnumRoutine.PENDULE),
        (EnumRoutine.PENDULE, EnumRoutine.SHAKER),
        (EnumPosition.POS_ARR_SKYMOULINETTE, EnumPosition.POS_PLONGEUR)
    ]