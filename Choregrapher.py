from enum import Enum
from EnumPosition import EnumPosition
from EnumPossibilite import EnumPossibilite
from Position import Position
from Routine import Routine
import random

class Choregrapher():
    """This is the Choregrapher for the Robot"""
    
    RPM_MOTOR = 114.0 #vitesse max moteur a vide

    def __init__(self) -> None:
        pass

    def createChoregraphy(self, musicLink : str) -> list:
        bpm = self.findBPM(musicLink)
        musicLength = 60
        positionsList = [EnumPosition.POS_INIT]
        execTime = EnumPosition.POS_INIT.time2Wait + EnumPosition.POS_INIT.time2Move * 2

        while(execTime < musicLength):    
            possibleMoveList = [item for item in EnumPossibilite.POSSIBILITIES if 1 in item]
            itemId = random.randint(0, len(possibleMoveList)-1)
            positionList.append(possibleMoveList[itemId])
            execTime += possibleMoveList[itemId].time2Move + possibleMoveList[itemId].time2Wait #voir pour récupérer time2mode & time2Wait depuis Routine (fonction ?)
            
        return positionList

    def findBPM(self, musicLink : str) -> int:
        return 132 

    def calBPMChoregraphy(self, choregraphy: tuple) -> None:
        previous = EnumPosition.POS_INIT.value.dicMotors
        for move in choregraphy:
            if(type(move) == Position):
                self.calBPMPerPosition(previous, move)
                previous = move
            elif(type(move) == Routine):
                for pos in move.lisPos:
                    self.calBPMPerPosition(previous, pos)
                    previous = pos

        
        #temps/bpm pour rappel
    
    def calBPMPerPosition(self, pos1: Position, pos2: Position) -> None:
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
        pos2.minSec = maxSec