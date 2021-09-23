from enum import Enum
from Position import Position


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
        time2Move=2,
        time2Wait=3
    )

    POS_SKYWATCHING = Position(
        dicMotors={
            'm1': 0,
            'm2': 0,
            'm3': 0,
            'm4': 0,
            'm5': -90,
            'm6': 0
        },
        time2Move=2,
        time2Wait=3
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
        time2Move=2,
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
        time2Move=1,
        time2Wait=0
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
        time2Move=1,
        time2Wait=0
    )

    # the position order of the shecker
    # first position for the initialisation
    POS_DEP_SHECKER = Position(
        dicMotors={
            'm1': -150,
            'm2': 0,
            'm3': 0,
            'm4': 0,
            'm5': 0,
            'm6': 0
        },
        time2Move=3,
        time2Wait=0
    )

    # first sheck
    POS_INTER_01_SHECKER = Position(
        dicMotors={
            'm1': -100,
            'm2': 0,
            'm3': 0,
            'm4': 0,
            'm5': 90,
            'm6': 0
        },
        time2Move=1,
        time2Wait=0
    )

    POS_INTER_02_SHECKER = Position(
        dicMotors={
            'm1': -50,
            'm2': 0,
            'm3': 0,
            'm4': 0,
            'm5': 0,
            'm6': 0
        },
        time2Move=1,
        time2Wait=0
    )

    POS_INTER_03_SHECKER = Position(
        dicMotors={
            'm1': 0,
            'm2': 0,
            'm3': 0,
            'm4': 0,
            'm5': 90,
            'm6': 0
        },
        time2Move=1,
        time2Wait=0
    )

    POS_INTER_04_SHECKER = Position(
        dicMotors={
            'm1': 50,
            'm2': 0,
            'm3': 0,
            'm4': 0,
            'm5': 0,
            'm6': 0
        },
        time2Move=1,
        time2Wait=0
    )

    POS_INTER_05_SHECKER = Position(
        dicMotors={
            'm1': 100,
            'm2': 0,
            'm3': 0,
            'm4': 0,
            'm5': 90,
            'm6': 0
        },
        time2Move=1,
        time2Wait=0
    )

    POS_ARR_SHECKER = Position(
        dicMotors={
            'm1': 150,
            'm2': 0,
            'm3': 0,
            'm4': 120,
            'm5': 0,
            'm6': 0
        },
        time2Move=1,
        time2Wait=0
    )

    POS_DEP_BALAYAGE = Position(
        dicMotors={
            'm1': 0,
            'm2': 90,
            'm3': 0,
            'm4': 0,
            'm5': -90,
            'm6': 0
        },
        time2Move=1,
        time2Wait=0
    )

    POS_1_BALAYAGE = Position(
        dicMotors={
            'm1': 90,
            'm2': 90,
            'm3': 0,
            'm4': 0,
            'm5': -90,
            'm6': 0
        },
        time2Move=1,
        time2Wait=0
    )

    POS_ARR_BALAYAGE = Position(
        dicMotors={
            'm1': -90,
            'm2': 90,
            'm3': 0,
            'm4': 0,
            'm5': -90,
            'm6': 0
        },
        time2Move=2,
        time2Wait=0
    )

    POS_DEP_PENDULE = Position(
        dicMotors={
            'm1': -150,
            'm2': 0,
            'm3': 90,
            'm4': 0,
            'm5': -90,
            'm6': 0
        },
        time2Move=3,
        time2Wait=1
    )

    POS_1_PENDULE = Position(
        dicMotors={
            'm1': -100,
            'm2': 0,
            'm3': 90,
            'm4': 90,
            'm5': -90,
            'm6': 0
        },
        time2Move=1,
        time2Wait=0
    )

    POS_2_PENDULE = Position(
        dicMotors={
            'm1': -50,
            'm2': 0,
            'm3': 90,
            'm4': -90,
            'm5': -90,
            'm6': 0
        },
        time2Move=1,
        time2Wait=0
    )

    POS_3_PENDULE = Position(
        dicMotors={
            'm1': 0,
            'm2': 0,
            'm3': 90,
            'm4': 90,
            'm5': -90,
            'm6': 0
        },
        time2Move=1,
        time2Wait=0
    )

    POS_4_PENDULE = Position(
        dicMotors={
            'm1': 50,
            'm2': 0,
            'm3': 90,
            'm4': -90,
            'm5': -90,
            'm6': 0
        },
        time2Move=1,
        time2Wait=0
    )

    POS_5_PENDULE = Position(
        dicMotors={
            'm1': 100,
            'm2': 0,
            'm3': 90,
            'm4': 90,
            'm5': -90,
            'm6': 0
        },
        time2Move=1,
        time2Wait=0
    )

    POS_ARR_PENDULE = Position(
        dicMotors={
            'm1': 150,
            'm2': 0,
            'm3': 90,
            'm4': -90,
            'm5': -90,
            'm6': 0
        },
        time2Move=1,
        time2Wait=0
    )

    POS_DEP_WAIT4IT = Position(
        dicMotors={
            'm1': 0,
            'm2': 0,
            'm3': -45,
            'm4': 0,
            'm5': 0,
            'm6': 0
        },
        time2Move=3,
        time2Wait=1
    )

    POS_1_WAIT4IT = Position(
        dicMotors={
            'm1': 0,
            'm2': 0,
            'm3': 0,
            'm4': 0,
            'm5': 0,
            'm6': 0
        },
        time2Move=1,
        time2Wait=0
    )

    POS_ARR_WAIT4IT = Position(
        dicMotors={
            'm1': 0,
            'm2': 0,
            'm3': 45,
            'm4': 0,
            'm5': -45,
            'm6': 0
        },
        time2Move=1,
        time2Wait=0
    )

    POS_DEP_SKYMOULINETTE = Position(
        dicMotors={
            'm1': -90,
            'm2': 0,
            'm3': 0,
            'm4': 90,
            'm5': -90,
            'm6': 0
        },
        time2Move=1,
        time2Wait=0
    )
