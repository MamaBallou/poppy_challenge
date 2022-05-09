# coding: utf8
class Position():
    """Position where Robot must move to.

    :param dict dicMotors: Motors dictionary referencing their position in
    degree angle.
    :param int time2Move: Moving time in seconde.
    :param int time2Wait: Waiting time at the end of deplacement in seconde.
    """

    def __init__(self, dicMotors: dict, time2Move: int,
                 time2Wait: int = 0) -> None:
        """Constructor"""
        self.dicMotors = dicMotors
