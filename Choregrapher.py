from enum import Enum
from EnumPosition import EnumPosition
from EnumPossibilite import EnumPossibilite
from EnumRoutine import EnumRoutine
from Position import Position
from Routine import Routine
from copy import copy
import random

class Choregrapher():
    """This is the Choregrapher for the Robot"""
    
    DPS_MOTOR = 114.0 * float(360.0 / 60.0) #vitesse max moteur a vide en degré par seconde
    secondPerBPM: float = 0.0

    def __init__(self) -> None:
        pass

    def createChoregraphy(self, musicLink : str) -> list:
        print("Create choregraphy")
        bpm = self.findBPM(musicLink)
        self.secondPerBPM = 60.0/float(bpm)
        musicLength = 60
        previous:EnumPosition|EnumRoutine = EnumPosition.POS_INIT
        positionsList: list[Position|Routine] = [copy(EnumPosition.POS_INIT.value)]
        execTime: float = 0.0
        rep = 0

        while(execTime < musicLength and rep < 10):
            rep += 1
            possibleMoveList: list[tuple[EnumPosition|EnumRoutine]] = [item for item in EnumPossibilite.POSSIBILITIES.value if previous in item]
            itemId = random.randint(0, len(possibleMoveList)-1)
            if(previous == possibleMoveList[itemId][0]):
                next:Position|Routine = copy(possibleMoveList[itemId][1].value)
                positionsList.append(next)
                execTime += self.checkAndCalcBPMForPositionOrRoutine(previous.value, next, possibleMoveList[itemId][1].value)
                previous = possibleMoveList[itemId][1]
            else:
                next:Position|Routine = copy(possibleMoveList[itemId][0].value)
                positionsList.append(next)
                execTime += self.checkAndCalcBPMForPositionOrRoutine(previous.value, next, possibleMoveList[itemId][0].value)
                previous = possibleMoveList[itemId][0]
        return positionsList

    def findBPM(self, musicLink : str) -> int:
        return 132 

    def checkAndCalcBPMForPositionOrRoutine(self, previous: Position|Routine, next: Position|Routine) -> float:
        previous = copy(previous)
        execTime: float = 0.0
        if(isinstance(next, Position)):
            execTime += self.calBPMPerPosition(previous, next)
        elif(isinstance(next, Routine)):
            for pos in next.lisPos:
                execTime += self.calBPMPerPosition(previous, pos)
                previous = pos
        # temps/bpm pour rappel
        return execTime
    
    def calBPMPerPosition(self, pos1: Position, pos2: Position) -> float:
        # Physic motor : 114 rpm
        maxSec = 0
        mot1 = pos1.dicMotors
        mot2 = pos2.dicMotors
        # Calculate max minimum moving time
        for motor in ("m1", "m2", "m3", "m4", "m5", "m6"):
            minMotor = abs(mot1[motor] - mot2[motor]) / self.DPS_MOTOR
            if(minMotor > maxSec):
                maxSec = minMotor
        # Set value move
        # Magic start here :) 
        # Ajouter le calcul
        multiplicatorTime2move = float(self.secondPerBPM) // float(maxSec)
        if (maxSec % self.secondPerBPM):
            multiplicatorTime2move += 1
        pos2.time2move = float(self.secondPerBPM) * float(multiplicatorTime2move)
        return pos2.time2move