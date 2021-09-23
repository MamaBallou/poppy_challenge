# coding: utf8
from Routine import Routine
from Position import Position
from _typeshed import Self
from pypot.creatures import PoppyErgoJr
import time, EnumPosition, EnumRoutine


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
            EnumRoutine.SHAKER,
            EnumPosition.POS_SKYWATCHING,
            EnumRoutine.SKY_MOULINETTE,
            EnumRoutine.PENDULE,
            EnumPosition.POS_PLONGEUR,
            EnumPosition.POS_REVERSE
        ]
        self.poppy = poppy

    def goPosition(self, position: Position) -> None:
        """To move poppy to Position.

        :param Position position: Position to move at.
        """
        # Making motors move and last wait its end to continu program.
        self.poppy.m1.goto_position(
            position.dicMotors["m1"], position.tempsDep)
        self.poppy.m2.goto_position(
            position.dicMotors["m2"], position.tempsDep)
        self.poppy.m3.goto_position(
            position.dicMotors["m3"], position.tempsDep)
        self.poppy.m4.goto_position(
            position.dicMotors["m4"], position.tempsDep)
        self.poppy.m5.goto_position(
            position.dicMotors["m5"], position.tempsDep)
        self.poppy.m6.goto_position(
            position.dicMotors["m6"], position.tempsDep, wait=True)
        # Wait the designated time.
        time.sleep(position.tempsAtt)

    def doRoutine(self, routine: Routine) -> None:
        """Execute de routine.

        :param Routine routine: Routine to execute.
        """
        # Go to starting position of the routine.
        # self.goPosition(routine.posInit)
        # Repeat the designated time the routine.
        for _ in range(routine.nbRep):
            # Going threw each steps of the routine.
            for pos in routine.lisPos:
                self.goPosition(pos)
            # End, go back to initial position.
            # self.goPosition(routine.posInit)

    
    def dance(self) -> None:
        """Execute the choregraphy."""
        # Read each instruction of choregraphy.
        for item in self.choregraphy:
            # Check type of item & use according function.
            if (isinstance(item, Position)):
                self.goPosition(item)
            elif (isinstance(item, Routine)):
                self.doRoutine(item)
