# coding: utf8
class Position():
    def __init__(self, dicMotors: dict, tempsDep: int, tempsAtt: int = 0) -> None:
        self.dicMotors = dicMotors
        self.tempsDep = tempsDep
        self.tempsAtt = tempsAtt
