from enum import Enum
import Position


class EnumPosition(Enum):
    POS_INIT = Position(
        dicMotors={
            'm1': 0,
            'm2': 0,
            'm3': 0,
            'm4': 0,
            'm5': 0,
            'm6': 0
        },
        time2Move=5,
        time2Wait=2
    )

    POS_REVERSE = Position(
        dicMotors={
            'm1': 0,
            'm2': 0,
            'm3': -90,
            'm4': 0,
            'm5': -90,
            'm6': 0
        },
        time2Move=5,
        time2Wait=2
    )

    POS_SKYWATCHING = Position(
        dicMotors={
            'm1': 0,
            'm2': 0,
            'm3': 0,
            'm4': 180,
            'm5': -90,
            'm6': 0
        },
        time2Move=5,
        time2Wait=2
    )

    POS_PLONGEUR = Position(
        dicMotors={
            'm1': 0,
            'm2': -45,
            'm3': 45,
            'm4': 0,
            'm5': -45,
            'm6': 0
        },
        time2Move=5,
        time2Wait=2
    )


    POS_DEP_LOOPING = Position(
        dicMotors={
            'm1': 0,
            'm2': -90,
            'm3': 0,
            'm4': 0,
            'm5': 90,
            'm6': 0
        },
        time2Move=5,
        time2Wait=2
    )
    

    POS_ARR_LOOPING = Position(
        dicMotors={
            'm1': 0,
            'm2': 0,
            'm3': -90,
            'm4': 0,
            'm5': -90,
            'm6': 0
        },
        time2Move=5,
        time2Wait=2
    )

    POS_DEP_SHACKER = Position(
        
    )
