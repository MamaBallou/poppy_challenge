# coding: utf8
class Position():
    """Position where Robot must move to.

    :param dict dicMotors: Motors dictionary referencing their position in
    degree angle.
    :param int time2Move: Moving time in seconde.
    :param int time2Wait: Waiting time at the end of deplacement in seconde.
    """

    def __init__(self, dicMotors: dict):
        """Constructor"""
        self.dicMotors = dicMotors
        self.minSec: float = 0.0