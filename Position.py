# coding: utf8
class Position():
    def __init__(self, dicMotors: dict, time2Move: int, time2Wait: int = 0) -> None:
        self.dicMotors = dicMotors
        self.time2Move = time2Move
        self.time2Wait = time2Wait
