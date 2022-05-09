# coding: utf8

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
        self.choregraphy = [
            EnumRoutine.WAIT4IT,
            EnumRoutine.BALAYAGE,
            EnumRoutine.LOOPING,
            EnumPosition.POS_REVERSE,
            EnumRoutine.PENDULE,
            EnumPosition.POS_SKYWATCHING,
            EnumRoutine.SKY_MOULINETTE,
            EnumPosition.POS_PLONGEUR,
            EnumRoutine.SHAKER
        ]
        self.poppy = poppy,
        self.time2move : int 

    def goPosition(self, position: EnumPosition) -> None:
        """To move poppy to Position.

        :param Position position: Position to move at.
        """
        print("goPosition(%s)", position.name)
        # Extracting Position from EnumPosition
        position = position.value
        # Making motors move and last wait its end to continu program.
        self.poppy.m1.goto_position(
            position.dicMotors["m1"], self.time2Move)
        self.poppy.m2.goto_position(
            position.dicMotors["m2"], self.time2Move)
        self.poppy.m3.goto_position(
            position.dicMotors["m3"], self.time2Move)
        self.poppy.m4.goto_position(
            position.dicMotors["m4"], self.time2Move)
        self.poppy.m5.goto_position(
            position.dicMotors["m5"], self.time2Move)
        self.poppy.m6.goto_position(
            position.dicMotors["m6"], self.time2Move, wait=True)
        # Wait the designated time.
        time.sleep(position.time2Wait)

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
        time2Move = 60.0/Choregrapher().findBPM(musicLink)
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
