# coding: utf8
from Challenge.Position import Position


class Routine():
    def __init__(self, lisPos: list, posInit: Position, nbRep: int = 1) -> None:
        self.lisPos = lisPos
        self.posInit = posInit
        self.nbRep = nbRep

    def __del__(self):
        del self.lisPos
        del self.posInit
