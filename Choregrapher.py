from enum import Enum
from EnumPosition import EnumPosition
from EnumPossibilite import EnumPossibilite
from Position import Position
from Routine import Routine
from copy import copy
import random

class Choregrapher():
    """This is the Choregrapher for the Robot"""
    
    RPM_MOTOR = 114.0 #vitesse max moteur a vide
    secondPerBPM: float = 0.0

    def __init__(self) -> None:
        pass

    def createChoregraphy(self, musicLink : str) -> list:
        print("Create choregraphy")
        bpm = self.findBPM(musicLink)
        self.secondPerBPM = 60.0/float(bpm)
        musicLength = 60
        previous: Position = EnumPosition.POS_INIT
        positionsList = [copy(EnumPosition.POS_INIT)]
        execTime: float = 0.0
        rep = 0

        while(execTime < musicLength and rep < 10):
            rep += 1
            print(positionsList)
            possibleMoveList = [item for item in EnumPossibilite.POSSIBILITIES.value if previous in item]
            itemId = random.randint(0, len(possibleMoveList)-1)
            if(previous == possibleMoveList[itemId][0]):
                next = copy(possibleMoveList[itemId][1])
                print("nextSet: ", type(next))
                positionsList.append(next)
                execTime += self.checkAndCalcBPMForPositionOrRoutine(previous, next, possibleMoveList[itemId][1].value)
            else:
                next = copy(possibleMoveList[itemId][0])
                positionsList.append(next)
                execTime += self.checkAndCalcBPMForPositionOrRoutine(previous, next, possibleMoveList[itemId][0].value)
            # TODO: enlever les mauvais truc et voir pour calculer le temps de déplacement au fur et à mesure plutôt et dans Robot
            print(execTime)
        return positionsList

    def findBPM(self, musicLink : str) -> int:
        return 132 

    def checkAndCalcBPMForPositionOrRoutine(self, previous: Position, next, templateNext) -> float:
        execTime: float = 0.0
        print("type", type(next))
        print(dir(next))
        if(isinstance(next.value, Position)):
            execTime += self.calBPMPerPosition(previous, next.value)
            previous = templateNext
        elif(isinstance(next.value, Routine)):
            for count, pos in enumerate(next.value.lisPos):
                execTime += self.calBPMPerPosition(previous, pos)
                previous = templateNext.lisPos[count]
        # temps/bpm pour rappel
        print("check: ", execTime)
        return execTime
    
    def calBPMPerPosition(self, pos1: Position, pos2: Position) -> float:
        # Physic motor : 114 rpm
        maxSec = 0
        mot1 = pos1.value.dicMotors
        mot2 = pos2.value.dicMotors
        # Calculate max minimum moving time
        for motor in ("m1", "m2", "m3", "m4", "m5", "m6"):
            minMotor = (abs(mot1[motor] - mot2[motor])/self.RPM_MOTOR)*60.0
            if(minMotor > maxSec):
                maxSec = minMotor
        # Set value move
        # Magic start here :) 
        # Ajouter le calcul
        multiplicatorTime2move = float(self.secondPerBPM) // float(maxSec)
        if (maxSec % self.secondPerBPM):
            multiplicatorTime2move += 1
        pos2.time2move= float(self.secondPerBPM) * float(multiplicatorTime2move)
        print("time2move: ", pos2.time2move)
        return pos2.time2move