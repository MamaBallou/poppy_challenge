# coding: utf8
class Position():
    """Position where Robot must move to.

    :param dict dicMotors: Motors dictionary referencing their position in
    degree angle.
    :param int time2Move: Moving time in seconde.
    :param int time2Wait: Waiting time at the end of deplacement in seconde.
    """

    def __init__(self, dicMotors: dict, time2move:float = 0.0):
        """Constructor"""
        self.dicMotors = dicMotors
        self.time2move: float = time2move
    
    def __str__(self):
        return f'dictMotor : {self.dicMotors}\ntime2move : {self.time2move}'