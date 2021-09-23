# coding: utf8
from Position import Position


class Routine():
    """A Routine is a sequence of positions repeated a designed number of time.

    :param list listPos: List of the positions the routine has to move at.
    :param Position posInit: Initial position of the routine.
    :param int npRep: Number of time the routine is repeated."""

    def __init__(self, posInit: Position, lisPos: list,
                 nbRep: int = 1) -> None:
        """Constructor"""
        self.lisPos = lisPos
        self.posInit = posInit
        self.nbRep = nbRep
