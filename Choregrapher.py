from EnumPosition import EnumPosition
from EnumPossibilite import EnumPossibilite
import random

class Choregrapher():
    """This is the Choregrapher for the Robot"""

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
        return 132 # calcul du temps par mouvement = 1/(bpm/60)