import random
class Reputation:
    def __init__(self, rep):
        self.reputation = rep

    def addRep(self, moreRep):
        self.reputation = self.reputation + moreRep
    
    def subRep(self, moreRep):
        self.reputation = self.reputation - moreRep
    
    def rep(self):
        return self.reputation
    
def repPick(word):
    rep = random.randint(len(word)-3, len(word)+6)
    return rep