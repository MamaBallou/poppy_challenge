from enum import Enum
import Routine
import EnumPosition


class EnumRoutine(Enum):
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
        ],
        1
    )

    LOOPING = Routine(
        None,
        [
            EnumPosition.POS_DEP_LOOPING,
            EnumPosition.POS_ARR_LOOPING
        ],
        1
    )

    BALAYAGE = Routine(
        None,
        [
            EnumPosition.POS_DEP_BALAYAGE,
            EnumPosition.POS_1_BALAYAGE,
            EnumPosition.POS_ARR_BALAYAGE,
            EnumPosition.POS_DEP_BALAYAGE
        ],
        1
    )

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
        ],
        1
    )

    WAIT4IT = Routine(
        None,
        [
            EnumPosition.POS_DEP_WAIT4IT,
            EnumPosition.POS_1_WAIT4IT,
            EnumPosition.POS_ARR_WAIT4IT
        ],
        1
    )

    SKY_MOULINETTE = Routine(
        None,
        [
            EnumPosition.POS_DEP_SKYMOULINETTE,
            EnumPosition.POS_SKYWATCHING
        ]
    )
