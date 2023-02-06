#Object Oriented Programming


#Treasure Chest

class TreasureChest():
    #PRIVATE question : STRING
    #PRIVATE answer : STRING
    #PRIVATE points : INTEGER


    def __init__(self,questionP,answerP,pointsP):
        self.question = questionP
        self.answer = answerP
        self.points = pointsP

    def getQuestion(self):
        return self.question

    def checkAnswer(self,Useranswer):
        if self.answer == Useranswer:
            return True
        else:
            return False


    def getPoints(self,NumAttempts):
        if NumAttempts == 1:
            return self.points
        elif NumAttempts == 2:
           return int(self.points//2)
        elif NumAttempts == 3 or NumAttempts == 4:
            return int(self.points//4)
        else:
            return 0




