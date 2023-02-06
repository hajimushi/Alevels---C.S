class baloon():

    # PRIVATE HEALTH : INTEGER
    # PRIVATE Colour : STRING
    # PRIVATE DefenceItem : STRING

    def __init__(self, ColourP, DefenceItemP):
        self.Health = 100
        self.Colour = ColourP
        self.DefenceItem = DefenceItemP

    def ChangeHealth(self, change):
        self.Health = self.Health + change

    def GetDefenceItem(self):
        return self.DefenceItem

    def CheckHealth(self):
        if self.Health <= 0:
            return True
        return False