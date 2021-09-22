# coding: utf8
class Position():
    def __init__(self, dicMotors: dict, tempsDep: int, tempsAtt: int = 0) -> None:
        self.dicMotors = dicMotors
        self.tempsDep = tempsDep
        self.tempsAtt = tempsAtt
    
    def posInit(self):
        self.dicMotors = {
            'm1': 0,
            'm2': 0,
            'm3': 0,
            'm4': 0,
            'm5': 0
        }

    def posReverse(self):
        self.dicMotors = {
            'm1': 0,
            'm2': 0,
            'm3': 0,
            'm4': 0,
            'm5': 0
        }

    def posSkyWatch(self):
        self.dicMotors = {
            'm1': 0,
            'm2': 0,
            'm3': 0,
            'm4': 0,
            'm5': 0
        }

    def posPlongeur(self):
        self.dicMotors = {
            'm1': 0,
            'm2': 0,
            'm3': 0,
            'm4': 0,
            'm5': 0
        }