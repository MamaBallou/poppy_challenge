# coding: utf8

from numpy import array
from Choregrapher import Choregrapher
from Routine import Routine
from Position import Position
from pypot.creatures import PoppyErgoJr
import time
from EnumPosition import EnumPosition
from EnumRoutine import EnumRoutine
import random


class Robot():
    """This is the Robot and its movements.

    :param list[Position|Routine] choregraphy: List of Routine & Position representing the choregraphy.
    :param PoppyErgoJr poppy: PoppyErgoJr robot object.
    """

    def __init__(self, poppy: PoppyErgoJr) -> None:
        """Constructor"""
        self.choregraphy = list
        self.poppy = poppy
        self.listLed= ['off','red','green','yellow','blue','pink','cyan','white']

    def goPosition(self, position: Position) -> None:
        """To move poppy to Position.

        :param Position position: Position to move at.
        """
        # Making motors move and last wait its end to continu program.
        self.poppy.m1.goto_position(
            position.dicMotors["m1"], position.time2move)
        self.poppy.m1.led=random.choice(self.listLed)

        self.poppy.m2.goto_position(
            position.dicMotors["m2"], position.time2move)
        self.poppy.m2.led=random.choice(self.listLed)

        self.poppy.m3.goto_position(
            position.dicMotors["m3"], position.time2move)
        self.poppy.m3.led=random.choice(self.listLed)

        self.poppy.m4.goto_position(
            position.dicMotors["m4"], position.time2move)
        self.poppy.m4.led=random.choice(self.listLed)

        self.poppy.m5.goto_position(
            position.dicMotors["m5"], position.time2move)
        self.poppy.m5.led=random.choice(self.listLed)

        self.poppy.m6.goto_position(
            position.dicMotors["m6"], position.time2move, wait=True)
        self.poppy.m6.led=random.choice(self.listLed)
        # Wait the designated time.

    def doRoutine(self, routine: Routine) -> None:
        """Execute de routine.

        :param Routine routine: Routine to execute.
        """
        # Repeat the designated time the routine.
        for _ in range(routine.nbRep):
            # Going threw each steps of the routine.
            for pos in routine.lisPos:
                self.goPosition(pos.value)

    def dance(self, musicLink: str) -> None:
        """Execute the choregraphy."""
        # Get time2move convert per second 60/bpm
        self.choregraphy = Choregrapher().createChoregraphy(musicLink)
        # Go to initial position
        self.goPosition(EnumPosition.POS_INIT.value)
        # Time start
        currentTime = time.time()
        # Read each instruction of choregraphy.
        for item in self.choregraphy:
            # Check type of item & use according function.
            if (isinstance(item, Position)):
                self.goPosition(item)
                for m in self.poppy.motors:
                    m.led=random.choice(self.listLed)
            elif (isinstance(item, Routine)):
                self.doRoutine(item)
                for m in self.poppy.motors:
                    m.led=random.choice(self.listLed)
        # Print lasting
        print(time.time() - currentTime)
        # Go backto initial position
        self.goPosition(EnumPosition.POS_INIT.value)
