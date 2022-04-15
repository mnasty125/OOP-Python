class Atm ():
    def __init__ (self, money):
        self.money=money
    def take_off (self, off):
        if (off <= self.money):
            self.money = self.money - off
        else:
            print ("Error")
    def get_refill (self, fill):
        self.money = self.money + fill
    def balance (self):
        print (self.money)

temp=Atm(300)
temp.take_off(100)
temp.get_refill(500)
temp.balance()