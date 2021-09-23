# coding: utf8
from Position import Position


class Routine():
    """A Routine is a sequence of positions repeated a designed number of time.

    :param list listPos: List of the positions the routine has to move at.
    :param Position posInit: Initial position of the routine.
    :param int npRep: Number of time the routine is repeated."""

    def __init__(self, lisPos: list, posInit: Position,
                 nbRep: int = 1) -> None:
        """Constructor"""
        self.lisPos = lisPos
        self.posInit = posInit
        self.nbRep = nbRep

    def __del__(self):
        """Destructor"""
        for pos in self.lisPos:
            del pos
        del self.posInit

    def shaker(self):
        self.posInit = Position(
            {
                'm1': -90,
                'm2': 0,
                'm3': 0,
                'm4': 180,
                'm5': 90,
            },
            5,
            5
        )
    
    def essuieGlace(self):
        self.posInit = Position(
            {
                'm1': 0,
                'm2': 90,
                'm3': 0,
                'm4': 0,
                'm5': -90,
            },
            5,
            5
        )
    
    def Looping(self):
        self.posInit = Position(
            {
                'm1': 0,
                'm2': 90,
                'm3': 90,
                'm4': 0,
                'm5': 180
            },
            5,
            5
        )