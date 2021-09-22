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