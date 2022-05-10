# coding: utf8

from numpy import array
from Choregrapher import Choregrapher
from Routine import Routine
from Position import Position
from pypot.creatures import PoppyErgoJr
import time
from EnumPosition import EnumPosition
from EnumRoutine import EnumRoutine


class Robot():
    """This is the Robot and its movements.

    :param list choregraphy: List of Routine & Position representing.
    :param PoppyErgoJr poppy: PoppyErgoJr robot object.
    """

    def __init__(self, poppy: PoppyErgoJr) -> None:
        """Constructor"""
        print(dir(EnumPosition.POS_INIT))
        self.choregraphy = list
        self.poppy = poppy
        self.time2move = float 
        self.nbBeatPerMv : int

    def goPosition(self, position: EnumPosition) -> None:
        """To move poppy to Position.

        :param Position position: Position to move at.
        """
        print("goPosition(%s)", position.name)
        # Extracting Position from EnumPosition
        pos = position.value
        # Making motors move and last wait its end to continu program.
        multiplicatorTime2move = float(pos.minSec) // float(self.time2move)
        print("minSec: ", pos.minSec)
        print("time2move: ", self.time2move)
        print("multiplicatorTime2move: ", multiplicatorTime2move)
        if (pos.minSec % self.time2move):
            multiplicatorTime2move += 1
        print("multiplicatorTime2move: ", multiplicatorTime2move)
        time2move = self.time2move * multiplicatorTime2move
        self.poppy.m1.goto_position(
            pos.dicMotors["m1"], time2move)
        self.poppy.m2.goto_position(
            pos.dicMotors["m2"], time2move)
        self.poppy.m3.goto_position(
            pos.dicMotors["m3"], time2move)
        self.poppy.m4.goto_position(
            pos.dicMotors["m4"], time2move)
        self.poppy.m5.goto_position(
            pos.dicMotors["m5"], time2move)
        self.poppy.m6.goto_position(
            pos.dicMotors["m6"], time2move, wait=True)
        # Wait the designated time.

    def doRoutine(self, routine: EnumRoutine) -> None:
        """Execute de routine.

        :param Routine routine: Routine to execute.
        """
        print("doRoutine(%s)", routine.name)
        # Extracting Routine from EnumRoutine
        routine = routine.value
        # Repeat the designated time the routine.
        for _ in range(routine.nbRep):
            # Going threw each steps of the routine.
            for pos in routine.lisPos:
                self.goPosition(pos)

    def dance(self, musicLink: str) -> None:
        """Execute the choregraphy."""
        # Get time2move convert per second 60/bpm
        self.nbBeatPerMv = 2
        self.time2move = (60.0/Choregrapher().findBPM(musicLink))*self.nbBeatPerMv
        self.choregraphy = Choregrapher().createChoregraphy(musicLink)
        # Go to initial position
        self.goPosition(EnumPosition.POS_INIT)
        # Time start
        currentTime = time.time()
        # Read each instruction of choregraphy.
        for item in self.choregraphy:
            # Check type of item & use according function.
            if (isinstance(item.value, Position)):
                self.goPosition(item)
            elif (isinstance(item.value, Routine)):
                self.doRoutine(item)
        # Print lasting
        print(time.time() - currentTime)
        # Go backto initial position
        self.goPosition(EnumPosition.POS_INIT)
