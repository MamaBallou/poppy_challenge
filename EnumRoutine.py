from enum import Enum
from Routine import Routine
from EnumPosition import EnumPosition


class EnumRoutine(Enum):
    """Enumeration of Routine."""

    # Shaking you up and down while turning.
    SHAKER = Routine(
        None,
        [
            EnumPosition.POS_DEP_SHECKER,
            EnumPosition.POS_INTER_01_SHECKER,
            EnumPosition.POS_INTER_02_SHECKER,
            EnumPosition.POS_INTER_03_SHECKER,
            EnumPosition.POS_INTER_04_SHECKER,
            EnumPosition.POS_INTER_05_SHECKER,
            EnumPosition.POS_ARR_SHECKER
        ]
    )

    # Start head up, finish head down.
    LOOPING = Routine(
        None,
        [
            EnumPosition.POS_DEP_LOOPING,
            EnumPosition.POS_ARR_LOOPING
        ]
    )

    # Close to the floor and left/right movements.
    BALAYAGE = Routine(
        None,
        [
            EnumPosition.POS_DEP_BALAYAGE,
            EnumPosition.POS_1_BALAYAGE,
            EnumPosition.POS_ARR_BALAYAGE,
            EnumPosition.POS_DEP_BALAYAGE
        ]
    )

    # Ocilating while turning.
    PENDULE = Routine(
        None,
        [
            EnumPosition.POS_DEP_PENDULE,
            EnumPosition.POS_1_PENDULE,
            EnumPosition.POS_2_PENDULE,
            EnumPosition.POS_3_PENDULE,
            EnumPosition.POS_4_PENDULE,
            EnumPosition.POS_5_PENDULE,
            EnumPosition.POS_ARR_PENDULE
        ]
    )

    # Suspens routine before big start.
    WAIT4IT = Routine(
        None,
        [
            EnumPosition.POS_DEP_WAIT4IT,
            EnumPosition.POS_1_WAIT4IT,
            EnumPosition.POS_ARR_WAIT4IT
        ]
    )

    # Turning while looking to the sky.
    SKY_MOULINETTE = Routine(
        None,
        [
            EnumPosition.POS_DEP_SKYMOULINETTE,
            EnumPosition.POS_ARR_SKYMOULINETTE
        ]
    )
