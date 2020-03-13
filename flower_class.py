# This is python program to make "flower" class.

class flower:
    def __init__(self):
        self.flower_name = None
        self.number_of_petals = None
        self.flower_price = None
    
    def setflower_name(self,flower_name):
        self.flower_name = flower_name
        
    def getflower_name(self):
        return self.flower_name
    
    def setnumber_of_petals(self,number_of_petals):
        self.number_of_petals = number_of_petals 
        
    def getnumber_of_petals(self):
        return self.number_of_petals

    def setflower_price(self,flower_price):
        self.flower_price = flower_price
        
    def getflower_price(self):
        return self.flower_price

    def show_flower_details(self):
        print("------------- FLOWER DETAIL -------------")
        print("flower name: {}".format(self.getflower_name()))
        print("Number of petals in flower: {}".format(self.getnumber_of_petals()))
        print("Price of flower is: Rs.{}".format(self.getflower_price()))


flower1 = flower()

flower_name = "Rose"
number_of_petals = 20
flower_price = 50 

flower1.setflower_name(flower_name)
flower1.setnumber_of_petals(number_of_petals)
flower1.setflower_price(flower_price)

flower1.show_flower_details()
print("-------------------------")
name  = flower1.getflower_name()
print("flower name:",name)