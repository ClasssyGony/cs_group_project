import random
class Reputation:
    def __init__(self, rep):
        self.reputation = rep

    def addRep(self, moreRep):
        self.reputation = self.reputation + moreRep
    
    def subRep(self, moreRep):
        self.reputation = self.reputation - moreRep