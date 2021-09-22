# coding: utf8
from Routine import Routine
from Position import Position
from _typeshed import Self
from pypot.creatures import PoppyErgoJr
import time

class Robot():
    """This is the Robot and its movements

    :param list choregraphy: List of Routine & Position representing

    :author: Mathilde Ballouhey
    """
    def __init__(self, choregraphy: list, poppy: PoppyErgoJr) -> None:
        """Constructeur"""
        self.choregraphy = choregraphy
        self.poppy = poppy
    
    def goPosition(self, position: Position) -> None:
        self.poppy.m1.goto_position(position.dicMotors["m1"], position.tempsDep)
        self.poppy.m2.goto_position(position.dicMotors["m2"], position.tempsDep)
        self.poppy.m3.goto_position(position.dicMotors["m3"], position.tempsDep)
        self.poppy.m4.goto_position(position.dicMotors["m4"], position.tempsDep)
        self.poppy.m5.goto_position(position.dicMotors["m5"], position.tempsDep)
        self.poppy.m6.goto_position(position.dicMotors["m6"], position.tempsDep, wait = True)

        time.sleep(position.tempsAtt)
    
    def doRoutine(self, routine: Routine):
        self.goPosition(routine.posInit)
        for _ in range(routine.nbRep):
            for pos in routine.lisPos:
                self.goPosition(pos)
            self.goPosition(routine.posInit)