import random
class Coin():
    def __init__ (self, count):
        self.count = count
        self.options = ['Heads' , 'Tails']
    def throw_once (self):
        heads_or_tails = random.choice(self.options)
        print(heads_or_tails)
    def throw (self):
        heads=0
        tails=0
        for i in range (self.count):
            heads_or_tails = random.choice(self.options)
            print(heads_or_tails)
            if (heads_or_tails == "Heads"):
                heads=heads+1
            elif (heads_or_tails == "Tails"):
                tails=tails+1
        print(heads, "/", tails)

temp=Coin(4)
temp.throw_once()
temp.throw()
